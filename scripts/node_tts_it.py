#!/usr/bin/python
# -*- coding:utf-8 -*-

import rospy
from std_msgs.msg import String
from gtts import gTTS
import os

tmpfile = "/tmp/output.mp3"

def speak_text(mytxt):
    try:
        mytxt.decode("utf-8")
        tts = gTTS(text=mytxt, lang='it', tld='com', slow=False, gender='female')
        tts.save(tmpfile)
        os.system(f"play {tmpfile}")
        os.remove(tmpfile)
    except Exception as e:
        print(f"Error occurred: {e}")

def callback(data):
    rospy.loginfo('Received message: %s', data.data)
    speak_text(data.data)

if __name__ == '__main__':
    rospy.init_node('speak_it_node', anonymous=True)
    rospy.Subscriber('speak_it', String, callback, queue_size=1)
    rospy.spin()
