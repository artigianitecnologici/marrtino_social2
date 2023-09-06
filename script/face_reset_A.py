#! /usr/bin/python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from threading import Timer

WIDTH  = rospy.get_param("/usbcam/image_width")
HEIGHT = rospy.get_param("/usbcam/image_height")

# time in seconds
TIME_DELAY = 5
rospy.set_param("face_reset_timer",TIME_DELAY)

IN_TOPIC = "/social/face_nroface"
IN_MSG   = Int32

OUT_TOPIC_TILT = "/tilt_controller/command"
OUT_TOPIC_PAN  = "/pan_controller/command" 
OUT_MSG = Float64

tilt_pub = rospy.Publisher(OUT_TOPIC_TILT,OUT_MSG,queue_size=1)
pan_pub = rospy.Publisher(OUT_TOPIC_PAN,OUT_MSG,queue_size=1)

tracking = False

def reset_face():    
    rospy.loginfo("Time is up, resetting face")
    tilt_pub.publish(Float64(0))
    pan_pub.publish(Float64(0))

t = Timer(TIME_DELAY,reset_face)
def restart_timer():
    global t
    t = Timer(TIME_DELAY,reset_face)
        
def start_timer():
    restart_timer()
    t.start()

def stop_timer():
    t.cancel()

def callback(data):
    global tracking
    if data.data == 0 and tracking:
        tracking = False
        rospy.loginfo("No faces detected, resetting face in {} seconds".format(TIME_DELAY))
        start_timer()

    elif data.data != 0 and not tracking:
        tracking = True
        rospy.loginfo("Detected faces, stopping timer if started")
        stop_timer()

def listener():
    rospy.init_node("face_reset_A")
    rospy.loginfo("Face reset start")
    rospy.Subscriber(IN_TOPIC,IN_MSG,callback)
    rospy.spin()

listener()
