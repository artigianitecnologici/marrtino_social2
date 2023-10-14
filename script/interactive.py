#! /usr/bin/python
import rospy
from std_msgs.msg import String

import threading
import requests
import sys,os
import time
import socket               # Import socket module
import os

from threading import Thread

SERVER_ADDRESS = '10.3.1.1'             # Get local machine name
SERVER_PORT = 9000                      # Reserve a port for your service.

sys.path.append(os.getenv("MARRTINO_APPS_HOME")+"/program")
from robot_cmd_ros import *


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
    rospy.loginfo("resetting face")
    #tilt_pub.publish(Float64(0))
    #pan_pub.publish(Float64(0))

def speech(msg,language):
    #rospy.loginfo('Speech : %s' %(msg))
    emotion("speak")
    say(msg,language)
    gesture('gesture')
    emotion("normal")



 
def timerping():
  threading.Timer(10.0, timerping).start()
  print("Ciao mondo!")
 


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


def command(msg):
    print(msg)
    t = Thread(target=run_code, args=(msg,))
    t.start()
    result = "ok"  

def listener():
    mylanguage = "it"
    begin()
    #rospy.init_node("interactive")
    print("Interactive Mode Start")
    #rospy.Subscriber(IN_TOPIC,IN_MSG,callback)
    reset_face()
    emotion("startblinking")
    gesture("gesture")
    speech("Ciao sono martina ",mylanguage)
    speech("Apri la applicazione e parla con me",mylanguage)
    connectionSocket, clientAddress = serverSocket.accept()
    myrequest = ""
    mycommand = ""
    myloop=True
    
    # try:
    count = 0
    #timerping()
    while myloop==True:
        # recv can throw socket.timeout
        #connectionSocket.settimeout(5.0)
       
        try:
            myrequest =  connectionSocket.recv(1024)
            
        except socket.timeout: # fail after 1 second of no activity
            print("Didn't receive data! [Timeout]")
        #finally:
            #s.close()
        
        print(myrequest)
        if (myrequest != ""):
            count += 1
            keyword = "martina"
            msglenght = len(myrequest)
            keylenght = len(keyword)
            mycommand = ""
            if (left(myrequest.lower(),keylenght) == keyword):
                mycommand =  myrequest[keylenght+1:msglenght]
                mycommand = mycommand.lower()

                print ("Comando " )
                print(mycommand)
                if ((mycommand == "parla inglese") or (mycommand == "speak english") or (mycommand == "you speak english")):
                    mylanguage = "en"
                    speech("i speak english now",mylanguage)

                if ((mycommand == "parla italiano") or (mycommand == "speak italian") or (mycommand == "you speak italian")):
                    mylanguage = "it"
                    speech("adesso parlo italiano",mylanguage)

                if ((mycommand == "alza le braccia") or (mycommand == "alza le mani") or  (mycommand == "raise your arms")):
                    gesture("up")

                if ((mycommand == "saluta") or (mycommand == "hello") or  (mycommand == "say hello")):
                    gesture("hello")

                if ((mycommand == "abbassa le braccia") or (mycommand == "abassa le mani")  or (mycommand == "lower your arms")):
                    gesture("down")
                
                if ((mycommand=="spengiti") or (mycommand == "spegniti" ) or (mycommand == "arresta il sistema")):
                    os.system("sudo halt")

                if (mycommand == "guarda avanti"):
                    pan(0)
                    tilt(0)
            
                if (mycommand == "voglio cercare un hotel"):
                    connectionSocket.send("https://www.booking.com")
                    speech("ti apro il sito di booking.com",mylanguage)

                if (mycommand == "aiuto"):
                    connectionSocket.send("https://social.marrtino.org/setup-robot/interactive-mode")
                    speech("ti apro il sito di marrtino",mylanguage)
           

            if myrequest=="stop":
                speech("ci vediamo alla prossima",mylanguage)
                myrequest=""
                myloop=False

            if myrequest=="fine":
                speech("ci vediamo alla prossima",mylanguage)
                myrequest=""
                myloop=False
            
            if myrequest=="PING":
                connectionSocket.send("PONG")
                myrequest=""
                
            
            if (myrequest != "" and mycommand == ""):
                connectionSocket.send("STOP")
                answer=bot(myrequest)
                print(answer)
                gesture("gesture")
                speech(answer,mylanguage)
                connectionSocket.send("SAY")

        
    print("Close connection on %d" % SERVER_PORT)
    connectionSocket.close()

    end()


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((SERVER_ADDRESS, SERVER_PORT))        # Bind to the port
serverSocket.listen(1)

print("Server waiting on (%s, %d)" % (SERVER_ADDRESS, SERVER_PORT))

listener()

