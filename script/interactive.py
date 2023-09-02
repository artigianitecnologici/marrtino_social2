#! /usr/bin/python
import requests
import sys,os
import time
import socket               # Import socket module

SERVER_ADDRESS = '10.3.1.1'             #           socket.gethostname() # Get local machine name
SERVER_PORT = 9000                      # Reserve a port for your service.

sys.path.append(os.getenv("MARRTINO_APPS_HOME")+"/program")
from robot_cmd_ros import *

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((SERVER_ADDRESS, SERVER_PORT))        # Bind to the port
serverSocket.listen(5)

print("Server waiting on (%s, %d)" % (SERVER_ADDRESS, SERVER_PORT))
connectionSocket, clientAddress = serverSocket.accept() 




myurl = 'http://10.3.1.1:5000/bot'
IN_TOPIC = "/social/face_nroface"
tracking = False

#
#  Gesture 
#

def gesture(mycmd):
    flagok = 0
    if (mycmd == 'posizione iniziale'):
        begin()
        spalla_flessione_dx(1.57)
        spalla_flessione_sx(3.663333333333333)
        spalla_rotazione_dx(2.965555555555556)
        spalla_rotazione_sx(2.267777777777778)
        gomito_dx(3.14)
        gomito_sx(2.0933333333333333)
        hand_right(2.6166666666666667)
        hand_left(2.6166666666666667)
        end()
        flagok = 1

    return flagok





def bot(msg):
    payload = {'query': msg}
    # Making a get request
    response =  requests.get(url = myurl, params=payload)
    content = response.content

    #print(content)
    return content

def left(s, n):
    return s[:n]


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

def wait_sec(nsec):
    t_end = time.time() + nsec
    myasr = ''
    while time.time() < t_end:
        myasr = ''
    

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
    mycommand = ""
    myloop=True
    # try:
    count = 0

    while myloop==True:

        myrequest =  connectionSocket.recv(1024)
        count += 1
        keyword = "comando:"
        msglenght = len(myrequest)
        keylenght = len(keyword)
        mycommand = ""
        if (left(myrequest,keylenght) == keyword):
            mycommand =  myrequest[keylenght+1:msglenght]
            #
            gesture("posizione iniziale")
            wait_sec(2)

            if (mycommand == 'alza le braccia'):
                spalla_flessione_dx(3.4016)
                spalla_flessione_sx(1.8316)
                gomito_dx(2.61)
                gomito_sx(2.61)

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
            speech(answer)
            connectionSocket.send("SAY")

        
    print("Close connection on %d" % SERVER_PORT)
    connectionSocket.close()
    end()
     
listener()
