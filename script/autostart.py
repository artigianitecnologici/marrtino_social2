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
    spalla_rotazione_dx(2.6166666666666667)
    spalla_flessione_dx(1.57)
    gomito_dx(3.14)
    hand_right(2.4422222222222225)
    hand_left(2.7911111111111113)
    spalla_rotazione_sx(2.6166666666666667)
    spalla_flessione_sx(3.663333333333333)
    gomito_sx(2.0933333333333333)


    # end command

    end()
     
listener()