#! /usr/bin/python
import rospy
from std_msgs.msg import String

import threading
import requests
import sys,os
import time
import socket               # Import socket module
import os
import random

from threading import Thread

SERVER_ADDRESS = '10.3.1.1'             # Get local machine name
SERVER_PORT = 9000                      # Reserve a port for your service.

sys.path.append(os.getenv("MARRTINO_APPS_HOME")+"/program")
from robot_cmd_ros import *


myurl = 'http://10.3.1.1:5000/bot'
#myurl = 'http://192.168.1.8:5000/bot'
IN_TOPIC = "/social/face_nroface"
OUT_GESTURE_TOPIC = "/social/gesture"
TOPIC_speech = "/speech/to_speak"
IN_TOPIC_speechstatus = "/speech/status"

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
    say(msg,language)
    gesture('gesture')
    

def callback_speechstatus(data):
    global stspeech
    stspeech = data.data
    if stspeech == "STOP":
        emotion("normal")
    if stspeech == "START":
        emotion("speak")

    rospy.loginfo(stspeech)
 
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

                value = random.randint(0, 13)
                if (value==0):
                    if (mylanguage == "it"):
                        speech("oggi non mi va proprio di fare niente",mylanguage)
                if (value==1):
                    if (mylanguage == "it"):
                        speech("ma perche non lo chiedi ad alexa o a googol",mylanguage)
                if (value==2):
                    if (mylanguage == "it"):
                        speech("basta co sta storia che i robot devono fare tutto quello che chiedi",mylanguage)
                    
                if (value==3):
                    if (mylanguage == "it"):
                        speech("oggi ho le cose mie quindi lasciami stare",mylanguage)
                        
               
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

                if ((mycommand == "saluta") or (mycommand == "saluto") or  (mycommand == "say hello")):
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
                    
                if ((mycommand.count("aiuto")> 0) or (mycommand.count("help")> 0)):
                    connectionSocket.send("https://social.marrtino.org/setup-robot/interactive-mode")
                    speech("ti apro il sito di marrtino",mylanguage)

                if (mycommand.count("robotica") > 0):
                    connectionSocket.send("https://www.robotics-3d.com")
                    speech("ti apro il sito di Robotics 3d che sono i migliori sul mercato",mylanguage)

                if ((mycommand == "hotel a firenze") or (mycommand == "hotel at florence")):
                    connectionSocket.send("https://www.booking.com/searchresults.it.html?ss=firenze&label=it-it-booking-desktop-VRZD0IC5lt9Ulq*ajTZ_bgS652829000338%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9181218%3Ali%3Adec%3Adm&aid=2311236&lang=it&sb=1&src_elem=sb&src=index&dest_id=-126693&dest_type=city&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure")
                    speech("ti apro il sito di Booking per fare la prenotazione",mylanguage)

                if ((mycommand == "quiz") or (mycommand == "apri il quiz")):
                    connectionSocket.send("http://10.3.1.1:8080/quiz/index.html")
                    speech("Adesso proviamo a fare il quizz insieme",mylanguage)

                if ((mycommand == "telepresenza") or (mycommand == "apri la telepresenza")):
                    connectionSocket.send("http://10.3.1.1:8080/social/navigation.php")
                    speech("Adesso puoi farmi camminare e vedere da remoto quello che vedo io",mylanguage)

                if ((mycommand == "Blocky") or (mycommand == "mi fai programmare")):
                    connectionSocket.send("http://10.3.1.1:8080/program/blockly_robot.php")
                    speech("Adesso facciamo programmazione estrema insieme",mylanguage)

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

