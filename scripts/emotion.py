#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

# Carica il classificatore per la rilevazione del volto e delle emozioni da OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
emotion_classifier = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'emotion.caffemodel')

class EmotionNode:
    def __init__(self):
        rospy.init_node('emotion_node')
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)

    def image_callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)
        for (x, y, w, h) in faces:
            roi_gray = gray_image[y:y + h, x:x + w]
            roi_color = cv_image[y:y + h, x:x + w]

            # Preprocess the face region for emotion recognition
            blob = cv2.dnn.blobFromImage(roi_gray, 1.0, (224, 224), (104, 117, 123))
            emotion_classifier.setInput(blob)
            predictions = emotion_classifier.forward()

            # Find the emotion with the highest probability
            emotion_label = emotions[max(enumerate(predictions[0]), key=lambda x: x[1])[0]]

            # Draw the emotion label on the face bounding box
            cv2.putText(cv_image, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        cv2.imshow('Emotion Detection', cv_image)
        cv2.waitKey(1)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
    emotion_node = EmotionNode()
    emotion_node.run()
