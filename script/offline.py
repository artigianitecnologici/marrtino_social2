#!/usr/bin/python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from std_msgs.msg import String
from threading import Timer
import time
import random

WIDTH  = rospy.get_param("/usbcam/image_width")
HEIGHT = rospy.get_param("/usbcam/image_height")

# time in seconds
TIME_DELAY = 60
rospy.set_param("face_reset_timer",TIME_DELAY)

IN_TOPIC = "/social/face_nroface"
IN_MSG   = Int32

# SOCIAL
# 
TOPIC_emotion = "social/emotion"
TOPIC_speech = "/speech/to_speak"
TOPIC_gesture = "/social/gesture"
OUT_GESTURE_TOPIC = "/social/gesture"


# publisher
emotion_pub = rospy.Publisher(TOPIC_emotion, String, queue_size=1,   latch=True)
speech_pub =rospy.Publisher(TOPIC_speech, String, queue_size=1,   latch=True)
gesture_pub = rospy.Publisher(OUT_GESTURE_TOPIC,String,queue_size=1)
# 
global tracking 

tracking = False


def gesture(msg):
    gesture_pub.publish(msg)


def say(msg):
    print('speech %s' %(msg))
    speech_pub.publish(msg)

def emotion(msg):
    print('social/emotion %s' %(msg))
    emotion_pub.publish(msg)


def speech(msg,language):
    #rospy.loginfo('Speech : %s' %(msg))
    emotion("speak")
    say(msg)
    gesture('gesture')
    emotion("normal")


def reset_face():
    global tracking
    rospy.loginfo("Time is up, resetting ..")
    tracking = False
    #tilt_pub.publish(Float64(0))
    #pan_pub.publish(Float64(0))

t = Timer(TIME_DELAY,reset_face)
def restart_timer():
    global t
    t = Timer(TIME_DELAY,reset_face)
    print("restart time")

def start_timer():
    restart_timer()
    t.start()

def stop_timer():
    t.cancel()

def callback(data):
    global tracking
    if data.data == 0 and tracking:
        #tracking = False
        #rospy.loginfo("No faces detected, resetting face in {} seconds".format(TIME_DELAY))
        start_timer()

    elif data.data != 0 and not tracking:
        tracking = True
        rospy.loginfo("Detected faces, stopping timer if started")

        value = random.randint(0, 3)
        if (value==0):
            gesture("hello")
        if (value==1):
            gesture("zero")  
        if (value==2):
            gesture("up")    
        if (value==3):
            gesture("down")    
    
        time.sleep(3)

        value = random.randint(0,13)
        if (value==0):
            speech("ciao io mi chiamo marrtina","it")

        if (value==1):
            speech("come va?","it") 

        if (value==2):
            speech("asta la vista","it")

        if (value==3):
            speech("hai visto a fabio?","it")           
        
        if (value==4):
            speech("io non sono pepper","it")

        if (value==5):
            speech("hai visto paolo?","it")

        if (value==6):
	        speech("ci conosciamo?","it")
        
        if (value==7):
	        speech("aloha","it")

        if (value==8):
 	        speech("mi raccomando non mi toccare","it")

        if (value==9):
	        speech("che fai di bello?","it")

        if (value==10):
            speech("sto cercando leonardo lo hai visto ?","it")

        if (value==11):
            speech("cosa ne pensi dell inteligenza artificiale?","it")

        if (value==12):
            speech("cosa ne pensi dei robot?","it")
        
        if (value==13):
            speech("sono bella?","it")


        time.sleep(3)
        stop_timer()

def listener():
    rospy.init_node("onair")
    rospy.loginfo("Start")
    rospy.Subscriber(IN_TOPIC,IN_MSG,callback)
    rospy.spin()

listener()

