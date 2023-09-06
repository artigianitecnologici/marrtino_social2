#! /usr/bin/python
import rospy
from std_msgs.msg import String

import requests
import sys,os
import time
import socket               # Import socket module
from threading import Thread

SERVER_ADDRESS = '10.3.1.1'             # Get local machine name
SERVER_PORT = 9000                      # Reserve a port for your service.

sys.path.append(os.getenv("MARRTINO_APPS_HOME")+"/program")
from robot_cmd_ros import *


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((SERVER_ADDRESS, SERVER_PORT))        # Bind to the port
serverSocket.listen(1)

print("Server waiting on (%s, %d)" % (SERVER_ADDRESS, SERVER_PORT))
connectionSocket, clientAddress = serverSocket.accept() 



myurl = 'http://10.3.1.1:5000/bot'
#myurl = 'http://192.168.1.8:5000/bot'
IN_TOPIC = "/social/face_nroface"
OUT_GESTURE_TOPIC = "/social/gesture"

tracking = False

gesture_pub = rospy.Publisher(OUT_GESTURE_TOPIC,String,queue_size=10)


def bot(msg):
    payload = {'query': msg}
    # Making a get request
    response =  requests.get(url = myurl, params=payload)
    content = response.content

    #print(content)
    return content

def left(s, n):
    return s[:n]

def gesture(msg):
    gesture_pub.publish(msg)

def reset_face():    
    rospy.loginfo("Time is up, resetting face")
    #tilt_pub.publish(Float64(0))
    #pan_pub.publish(Float64(0))

def speech(msg):
    #rospy.loginfo('Speech : %s' %(msg))
    emotion("speak")
    say(msg,'it')
    #
    gesture('gesture')
    #speak_it_pub.publish(msg.decode("utf-8"))
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

def command(msg):
    print(msg)
    t = Thread(target=run_code, args=(msg,))
    t.start()
    result = "ok"  

def listener():
    begin()
    #rospy.init_node("interactive")
    print("Interactive Mode Start")
    #rospy.Subscriber(IN_TOPIC,IN_MSG,callback)
    reset_face()
    emotion("startblinking")
    gesture("gesture")
    speech("Ciao sono martina se vuoi puoi parlare con me")
    speech("dimmi")
    myrequest = ""
    mycommand = ""
    myloop=True
    # try:
    count = 0

    while myloop==True:

        myrequest =  connectionSocket.recv(1024)
        #print(myrequest)
        count += 1
        keyword = "martina"
        msglenght = len(myrequest)
        keylenght = len(keyword)
        mycommand = ""
        if (left(myrequest.lower(),keylenght) == keyword):
            mycommand =  myrequest[keylenght+1:msglenght]
            mycommand = mycommand.lower()
            if (mycommand == "alza le braccia"):
                spalla_flessione_dx(2.6166666666666667)
                spalla_flessione_sx(2.6166666666666667)
            if (mycommand == "guarda avanti"):
                pan(0)
                tilt(0)

        if myrequest=="stop":
            speech("ci vediamo alla prossima")
            myrequest=""
            myloop=False

        if myrequest=="fine":
            speech("ci vediamo alla prossima")
            myrequest=""
            myloop=False
            
            
        if (myrequest != "" and mycommand == ""):
            connectionSocket.send("STOP")
            answer=bot(myrequest)
            print(answer)
            gesture("gesture")
            speech(answer)
            connectionSocket.send("SAY")

        
    print("Close connection on %d" % SERVER_PORT)
    connectionSocket.close()

    end()
     
listener()
