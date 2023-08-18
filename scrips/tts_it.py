#!/usr/bin/python
# -*- coding:utf-8 -*-
import rospy 
from std_msgs.msg import String
from gtts import gTTS
import os
from subprocess import Popen, PIPE
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
tmpfile = "/tmp/cacheita.mp3"

def callback(data):
    rospy.loginfo('I heard %s', data.data)
    try:
        mytxt = data.data
        mytxt.decode("utf-8")
        tts = gTTS(mytxt, lang='it')
        tts.save(tmpfile)
        pitch = "600"
        p=Popen("play " + tmpfile + " -q pitch 600" , stdout=PIPE, shell=True)
        #"play " +  filename + " -q" + pitch + bass + treble + volume; 
        p.wait()
        os.remove(tmpfile)
    except Exception as e:
        print("receive msg,but parse exception:", e)

if __name__ == '__main__':
    rospy.init_node('marrtino_speack_it_node', anonymous=True)
    rospy.Subscriber('speak_it', String, callback, queue_size=1)
    rospy.spin()