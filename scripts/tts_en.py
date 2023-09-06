#!/usr/bin/python
# -*- coding:utf-8 -*-

import rospy 
from std_msgs.msg import String
from gtts import gTTS
import os
from subprocess import Popen, PIPE
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
tmpfile = "/tmp/cacheen.mp3"


def callback(data):
    rospy.loginfo('I heard %s', data.data)
    try:
        tts = gTTS(text=data.data, lang='it')
        tts.save(tmpfile)
        pitch = "600"
        p=Popen("play " + tmpfile + " -q pitch 600" , stdout=PIPE, shell=True)
        p.wait()
        os.remove(tmpfile)
    except Exception as e:
        print("receive msg,but parse exception:", e)

if __name__ == '__main__':
    rospy.init_node('marrtino_speak_en_node', anonymous=True)
    rospy.Subscriber('speak_en', String, callback, queue_size=1)
    rospy.spin()