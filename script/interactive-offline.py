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
import json

from threading import Thread

SERVER_ADDRESS = '10.3.1.1'             # Get local machine name
SERVER_PORT = 9000                      # Reserve a port for your service.

#sys.path.append(os.getenv("MARRTINO_APPS_HOME")+"/program")
#from robot_cmd_ros import *


myurl = 'http://10.3.1.1:5000/bot'
#myurl = 'http://192.168.1.8:5000/bot'
IN_TOPIC = "/social/face_nroface"
TOPIC_asr = "/social/asr"
TOPIC_gesture = "/social/gesture"
TOPIC_emotion = "social/emotion"
TOPIC_speech = "/speech/to_speak"
IN_TOPIC_speechstatus = "/speech/status"

tracking = False

gesture_pub = rospy.Publisher(TOPIC_gesture,String,queue_size=10)
emotion_pub = rospy.Publisher(TOPIC_emotion, String, queue_size=1,   latch=True)
speech_pub =rospy.Publisher(TOPIC_speech, String, queue_size=1,   latch=True)

global asr_request,stspeech
asr_request = ""
stspeech = ""
mylanguage = "it"

def say(msg,language):
    print('speech %s' %(msg))
    speech_pub.publish(msg)

def emotion(msg):
    #
    print('social/emotion %s' %(msg))
    emotion_pub.publish(msg)

def bot(msg):
    payload = {'query': msg}
    rospy.loginfo('query %s' %(msg))
    # Making a get request
    response =  requests.get(url = myurl, params=payload)
    content = response.content
    #print(content)

    return content

def left(s, n):
    return s[:n]

def gesture(msg):
    gesture_pub.publish(msg)

def speech(msg,language):
    #rospy.loginfo('Speech : %s' %(msg))
    say(msg,language)
    gesture('gesture')
    

 
def callback_asr(data):
    global asr_request, stspeech
    myasr = data.data
    if stspeech == "STOP":
        asr_request =  myasr
        request(asr_request)
        rospy.loginfo(asr_request)
 
def callback_speechstatus(data):
    global stspeech
    stspeech = data.data
    if (stspeech=='STOP'):
        emotion("normal")
    if (stspeech=='START'):
        emotion("speak")
    rospy.loginfo(stspeech)

    # call 
def request(myrequest):
    count = 0
    global mylanguage 
        
    if (myrequest != ""):
        count += 1
        keyword = "martina"
        msglenght = len(myrequest)
        keylenght = len(keyword)
        mycommand = ""

        flrequest = True
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
                flrequest = False

            if ((mycommand == "parla italiano") or (mycommand == "speak italian") or (mycommand == "you speak italian")):
                mylanguage = "it"
                speech("adesso parlo italiano",mylanguage)
                flrequest = False


            if ((mycommand == "alza le braccia") or (mycommand == "alza le mani") or  (mycommand == "raise your arms")):
                gesture("up")
                flrequest = False


            if ((mycommand == "saluta") or (mycommand == "saluto") or  (mycommand == "say hello")):
                gesture("hello")
                flrequest = False


            if ((mycommand == "abbassa le braccia") or (mycommand == "abassa le mani")  or (mycommand == "lower your arms")):
                gesture("down")
                flrequest = False

            
            if ((mycommand=="spengiti") or (mycommand == "spegniti" ) or (mycommand == "arresta il sistema")):
                os.system("sudo halt")
                flrequest = False


            if (mycommand == "guarda avanti"):
                pan(0)
                tilt(0)
                flrequest = False

            if (mycommand == "voglio cercare un hotel"):
                #connectionSocket.send("https://www.booking.com")
                speech("ti apro il sito di booking.com",mylanguage)
                flrequest = False

                
            if ((mycommand.count("aiuto")> 0) or (mycommand.count("help")> 0)):
                #connectionSocket.send("https://social.marrtino.org/setup-robot/interactive-mode")
                speech("ti apro il sito di marrtino",mylanguage)
                flrequest = False


            if (mycommand.count("robotica") > 0):
                #connectionSocket.send("https://www.robotics-3d.com")
                speech("ti apro il sito di Robotics 3d che sono i migliori sul mercato",mylanguage)
                flrequest = False

            if ((mycommand == "hotel a firenze") or (mycommand == "hotel at florence")):
                #connectionSocket.send("https://www.booking.com/searchresults.it.html?ss=firenze&label=it-it-booking-desktop-VRZD0IC5lt9Ulq*ajTZ_bgS652829000338%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9181218%3Ali%3Adec%3Adm&aid=2311236&lang=it&sb=1&src_elem=sb&src=index&dest_id=-126693&dest_type=city&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure")
                speech("ti apro il sito di Booking per fare la prenotazione",mylanguage)
                flrequest = False


            if ((mycommand == "quiz") or (mycommand == "apri il quiz")):
                #connectionSocket.send("http://10.3.1.1:8080/quiz/index.html")
                speech("Adesso proviamo a fare il quizz insieme",mylanguage)
                flrequest = False

            if ((mycommand == "telepresenza") or (mycommand == "apri la telepresenza")):
                #connectionSocket.send("http://10.3.1.1:8080/social/navigation.php")
                speech("Adesso puoi farmi camminare e vedere da remoto quello che vedo io",mylanguage)
                flrequest = False

            if ((mycommand == "Blocky") or (mycommand == "mi fai programmare")):
                #connectionSocket.send("http://10.3.1.1:8080/program/blockly_robot.php")
                speech("Adesso facciamo programmazione estrema insieme",mylanguage)
                flrequest = False

            if (flrequest== True):
                #connectionSocket.send("STOP")
                answer=bot(mycommand)
                print(answer)
                speech(answer,mylanguage)
                #connectionSocket.send("SAY")

        # 

        if myrequest=="stop":
            speech("ci vediamo alla prossima",mylanguage)
            myrequest=""
            myloop=False

        if myrequest=="fine":
            speech("ci vediamo alla prossima",mylanguage)
            myrequest=""
            myloop=False
        
        if myrequest=="PING":
            #connectionSocket.send("PONG")
            myrequest=""
            


def listener():

    mylanguage = "it"
    #begin()
    rospy.init_node("interactive")
    print("Interactive Mode Start")
    rospy.Subscriber(TOPIC_asr,String,callback_asr)
    rospy.Subscriber(IN_TOPIC_speechstatus,String,callback_speechstatus)
    emotion("startblinking")
    gesture("gesture")
    speech("Ciao sono martina ",mylanguage)
    speech("mi raccomando chiamami per nome quando ti rivolgi a me",mylanguage)

    
  


    rospy.spin()


listener()

