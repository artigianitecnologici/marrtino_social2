#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from depthai_sdk import OakCamera, TextPosition, Visualizer
from depthai_sdk.classes.packets  import TwoStagePacket
import numpy as np
import cv2 

class PedestrianReId:
    def __init__(self) -> None:
        self.results = []

    def _cosine_dist(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def new_result(self, vector_result) -> int:
        vector_result = np.array(vector_result)
        for i, vector in enumerate(self.results):
            dist = self._cosine_dist(vector, vector_result)
            if dist > 0.7:
                self.results[i] = vector_result
                return i
        else:
            self.results.append(vector_result)
            return len(self.results) - 1
        

rospy.init_node("node_followme")
# Publisher
# pubFaceEmotion = rospy.Publisher("FaceEmotion", String, queue_size=10)

with OakCamera() as oak:
    color = oak.create_camera('color', fps=10)

    person_det = oak.create_nn('person-detection-retail-0013', color)
    person_det.node.setNumInferenceThreads(2)
    person_det.config_nn(resize_mode='crop')

    nn_reid = oak.create_nn('person-reidentification-retail-0288', input=person_det)
    nn_reid.node.setNumInferenceThreads(2)

    reid = PedestrianReId()
    results = []


    def cb(packet: TwoStagePacket):
        visualizer = packet.visualizer
        for det, rec in zip(packet.detections, packet.nnData):
            reid_result = rec.getFirstLayerFp16()
            id = reid.new_result(reid_result)
            # posx = det.top_right-det.top_left
           #  posy = det.bottom_right-det.top_right



            visualizer.add_text(f"ID: {id}",
                                bbox=(*det.top_left, *det.bottom_right),
                                position=TextPosition.MID)
        frame = visualizer.draw(packet.frame)
        cv2.imshow('Person reidentification', frame)

    oak.visualize(nn_reid, callback=cb, fps=True)
    # oak.show_graph()
    oak.start(blocking=True)

    color = oak.create_camera('color')
    det_nn = oak.create_nn('face-detection-retail-0004', color)
    # Passthrough is enabled for debugging purposes
    # AspectRatioResizeMode has to be CROP for 2-stage pipelines at the moment
    det_nn.config_nn(resize_mode='crop')

    emotion_nn = oak.create_nn('emotions-recognition-retail-0003', input=det_nn)
    # emotion_nn.config_multistage_nn(show_cropped_frames=True) # For debugging

    def cb(packet: TwoStagePacket):
        vis: Visualizer = packet.visualizer
        for det, rec in zip(packet.detections, packet.nnData):
            emotion_results = np.array(rec.getFirstLayerFp16())
            emotion_name = emotions[np.argmax(emotion_results)]
            rospy.loginfo(emotion_name)
            pubFaceEmotion.publish(emotion_name)
            vis.add_text(emotion_name,
                            bbox=(*det.top_left, *det.bottom_right),
                            position=TextPosition.BOTTOM_RIGHT)

        vis.draw(packet.frame)
        cv2.imshow(packet.name, packet.frame)


    # Visualize detections on the frame. Also display FPS on the frame. Don't show the frame but send the packet
    # to the callback function (where it will be displayed)
    oak.visualize(emotion_nn, callback=cb, fps=True)
    oak.visualize(det_nn.out.passthrough)
    # oak.show_graph() # Show pipeline graph
    oak.start(blocking=True) # This call will block until the app is stopped (by pressing 'Q' button)
