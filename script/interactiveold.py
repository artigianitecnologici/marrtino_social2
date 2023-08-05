#! /usr/bin/python
import requests
import sys,os
import time



sys.path.append(os.getenv("MARRTINO_APPS_HOME")+"/program")

from robot_cmd_ros import *

myurl = 'http://10.3.1.1:5000/bot'
IN_TOPIC = "/social/face_nroface"
tracking = False

def bot(msg):
    payload = {'query': msg}
    # Making a get request
    response =  requests.get(url = myurl, params=payload)
    content = response.content

    #print(content)
    return content



def reset_face():    
    rospy.loginfo("Time is up, resetting face")
    #tilt_pub.publish(Float64(0))
    #pan_pub.publish(Float64(0))

def speech(msg):
    #rospy.loginfo('Speech : %s' %(msg))
    emotion("speak")
    say(msg,'it')
    emotion("normal")

def callback(data):
    global tracking
    if data.data == 0 and tracking:
        tracking = False
        #rospy.loginfo("No faces detected, resetting face in {} seconds".format(TIME_DELAY))
        #start_timer()

    elif data.data != 0 and not tracking:
        tracking = True
        #rospy.loginfo("Detected faces, stopping timer if started")
        speech("ciao")
        #stop_timer()

def wait_user_speaking(nsec):
    t_end = time.time()+nsec
    myasr = ''
    while time.time() < t_end:
        if myasr == '' :
            myasr = asr()    
        else :
            break
        return myasr
    

def listener():
    begin()
    #rospy.init_node("interactive")
    print("Interactive Mode Start")
    #rospy.Subscriber(IN_TOPIC,IN_MSG,callback)
    reset_face()
    emotion("startblinking")
    speech("Ciao sono martina se vuoi puoi parlare con me")
    speech("dimmi")
    myrequest = ""
    myloop=True
    # try:
    count = 0
    while myloop==True:
        myrequest = wait_user_speaking(5)
        count += 1
        if myrequest=="stop":
            speech("ci vediamo alla prossima")
            myrequest=""
            myloop=False

        if myrequest=="fine":
            speech("ci vediamo alla prossima")
            myrequest=""
            myloop=False
            
        if (myrequest != ""):
            answer=bot(myrequest)
            print(answer)
            speech(answer)
        

   

 
        
    end()
     
listener()
