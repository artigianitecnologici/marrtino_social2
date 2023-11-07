#!/usr/bin/python
# -*- coding:utf-8 -*-

import rospy
from std_msgs.msg import String
import time
import os
import sounddevice as sd
#import alsaaudio
#sudo apt-get install libttspico-utils



def listdevice():
    # list all audio devices known to your system
    print("Display input/output devices")
    print(sd.query_devices())

def setdefaultdevice(devout):
    sd.default.device = devout

tmpfile = "/tmp/output.wav"



def speak_text(mytxt):
    try:
        lang="it-IT"
        cmd = 'pico2wave -l "%s" -w %s " , %s"' %(lang,tmpfile, mytxt)
        print(cmd)
        os.system(cmd)
        time.sleep(0.2)
        cmd = "play %s" % tmpfile
        os.system(cmd)
        
        os.remove(tmpfile)
    except Exception as e:
        print("Error occurred: ")

def callback(data):
    rospy.loginfo('Received message: %s', data.data)
    speak_text(data.data)

if __name__ == '__main__':
    #init_alsaaudio()
    
    #rospy.init_node('speak_it_node', anonymous=True)
    #rospy.Subscriber('speak_it', String, callback, queue_size=1)
    #rospy.spin()
    listdevice()
    setdefaultdevice(1)
    speak_text("Io sono marrtina e sono un robot sociale")
    setdefaultdevice(2)
    speak_text("Io sono marrtina e sono un robot sociale")
    setdefaultdevice(3)
    speak_text("Io sono marrtina e sono un robot sociale")
    setdefaultdevice(4)
    speak_text("Io sono marrtina e sono un robot sociale")
    setdefaultdevice(5)
    speak_text("Io sono marrtina e sono un robot sociale")