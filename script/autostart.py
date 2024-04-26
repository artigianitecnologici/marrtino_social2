#! /usr/bin/python
import requests
import sys,os
import time

sys.path.append(os.getenv("MARRTINO_APPS_HOME")+"/program")


from robot_cmd_ros import *

def speech(msg):
    #rospy.loginfo('Speech : %s' %(msg))
    emotion("speak")
    say(msg,'it')
    emotion("normal")
    

def listener():
    begin()
   
    
    print("Start MARRTINA Robot")
    
    # start command here
    emotion("startblinking")
    speech("Ciao sono martina e sono operativa")
   
    pan(0)
    tilt(0) 
    # 
    right_shoulder_flexion(-70)
    left_shoulder_flexion(-70)
    right_shoulder_rotation(0)
    left_shoulder_rotation(0)
    right_elbow(0)
    left_elbow(0)
    right_hand(90)
    left_hand(90)


    # end command

    end()
     
listener()