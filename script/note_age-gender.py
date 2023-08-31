#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from depthai_sdk import OakCamera, TextPosition, Visualizer
from depthai_sdk.classes.packets  import TwoStagePacket
import numpy as np
import cv2 

rospy.init_node("node-age-gender")
# Publisher
#pubFaceEmotion = rospy.Publisher("social/faceemotion", String, queue_size=10)
pubAge = rospy.Publisher("social/age", String, queue_size=10)
pubGender = rospy.Publisher("social/gender", String, queue_size=10)
with OakCamera() as oak:
    color = oak.create_camera('color')
    det_nn = oak.create_nn('face-detection-retail-0004', color)
    # Passthrough is enabled for debugging purposes
    # AspectRatioResizeMode has to be CROP for 2-stage pipelines at the moment
    det_nn.config_nn(resize_mode='crop')

    #emotion_nn = oak.create_nn('emotions-recognition-retail-0003', input=det_nn)
    age_gender = oak.create_nn('age-gender-recognition-retail-0013', input=det_nn)

    def cb(packet: TwoStagePacket):
        vis: Visualizer = packet.visualizer
        for det, rec in zip(packet.detections, packet.nnData):
            age = int(float(np.squeeze(np.array(rec.getLayerFp16('age_conv3')))) * 100)
            gender = np.squeeze(np.array(rec.getLayerFp16('prob')))
            gender_str = "woman" if gender[0] > gender[1] else "man"
            #emotion_results = np.array(rec.getFirstLayerFp16())
            #emotion_name = emotions[np.argmax(emotion_results)]
            rospy.loginfo('------')
            #rospy.loginfo(emotion_name)
            #rospy.loginfo(age)
            #rospy.loginfo(gender)
            #pubFaceEmotion.publish(emotion_name)

            vis.add_text(f'{gender_str}\nage: {age}',
                                bbox=(*det.top_left, *det.bottom_right),
                                position=TextPosition.BOTTOM_RIGHT)

        vis.draw(packet.frame)
        cv2.imshow(packet.name, packet.frame)


    # Visualize detections on the frame. Don't show the frame but send the packet
    # to the callback function (where it will be displayed)
    oak.visualize(age_gender, callback=cb).detections(fill_transparency=0.1)
    oak.visualize(det_nn.out.passthrough)
    oak.visualize(age_gender.out.twostage_crops, scale=3.0)
