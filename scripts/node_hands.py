#!/usr/bin/env python3
import rospy
import cv2
import mediapipe as mp
from google.protobuf.json_format import MessageToDict
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

# Inizializzazione del modello
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2
)

cvbridge = CvBridge()
# Publisher
pubHands = rospy.Publisher("hands", String, queue_size=10)


# Funzione di callback per l'immagine
def image_callback(data):
    try:
        cv_image = cvbridge.imgmsg_to_cv2(data, "bgr8")
        img = cv2.flip(cv_image, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            if len(results.multi_handedness) == 2:
                print('Both Hands')
                pubHands.publish('Both')
            else:
                for i in results.multi_handedness:
                    label = MessageToDict(i)['classification'][0]['label']
                    #print(label)
                    if (label != ''):
                        print(label)
                        pubHands.publish(label)
        #cv2.imshow('Image', img_rgb)
        #cv2.waitKey(1)
    except CvBridgeError as e:
        print(e)

# Funzione per identificare automaticamente il topic dell'immagine
def auto_image_topic():
    topics = rospy.get_published_topics()
    for t in topics:
        if t[1] == 'sensor_msgs/Image' and 'depth' not in t[0] and '/ir/' not in t[0] \
           and 'person' not in t[0] and 'tag' not in t[0]:
            return t[0]
    return None

def main():
    rospy.init_node('node_hands')
   
    image_topic = auto_image_topic()
    if image_topic is not None:
        sub_image = rospy.Subscriber(image_topic, Image, image_callback)
        rospy.spin()
    else:
        print("Image topic not found.")

if __name__ == "__main__":
    main()
