#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String
import threading
import requests
import sys, os
import time
import socket
import random
import json  # Import per decodifica JSON

from threading import Thread

SERVER_ADDRESS = '10.3.1.1'
SERVER_PORT = 9000

sys.path.append(os.getenv("MARRTINO_APPS_HOME")+"/program")
from robot_cmd_ros import *

myurl = 'http://10.3.1.1:5000/bot'
TOPIC_nroface = "/social/face_nroface"
TOPIC_gesture = "/social/gesture"
TOPIC_speech = "/social/speech/to_speak"
TOPIC_speechstatus = "/social/speech/status"
TOPIC_language = "/social/speech/language"
TOPIC_emotion = "/social/emotion"
TOPIC_response_gtp = "/gtpresponse"
TOPIC_request_gtp = "/gtprequest"

tracking = False

gesture_pub = rospy.Publisher(TOPIC_gesture, String, queue_size=10)
emotion_pub = rospy.Publisher(TOPIC_emotion, String, queue_size=1, latch=True)
gpt_request_publisher = rospy.Publisher(TOPIC_request_gtp, String, queue_size=10)
speech_pub =  rospy.Publisher(TOPIC_speech, String, queue_size=1,   latch=True)
language_pub = rospy.Publisher(TOPIC_language, String, queue_size=1,   latch=True)

# Funzione di connessione socket con gestione degli errori
def create_server_socket(server_address, server_port, retries=5, retry_delay=5):
    while retries > 0:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((server_address, server_port))
            server_socket.listen(1)
            print "Server listening on (%s, %d)" % (server_address, server_port)
            return server_socket
        except socket.error as e:
            if e.errno == 98:  # Address already in use
                print "Errore: Indirizzo già in uso. Riprovo a collegarmi tra %d secondi..." % retry_delay
                time.sleep(retry_delay)
                retries -= 1
            else:
                print "Errore di socket: %s" % e
                raise e
    raise RuntimeError("Impossibile avviare il server socket dopo vari tentativi")

def callback_gtpresponse(msg):
    try:
        json_data = json.loads(msg.data)
        rospy.loginfo("Messaggio decodificato ricevuto:")
        rospy.loginfo(json.dumps(json_data, indent=4, ensure_ascii=False))

        # Helper function per estrarre il primo elemento se è una lista
        def extract_first_element(value):
            if isinstance(value, list) and len(value) > 0:
                return value[0]  # Restituisce il primo elemento della lista
            return value  # Se non è una lista, restituisce il valore così com'è

        status = json_data.get("status", "N/A")
        msg_field = json_data.get("msg", "N/A")
        error = json_data.get("error", "N/A")
        data = json_data.get("data", {})
        action = json_data.get("action", "N/A")

        macro_vr = extract_first_element(data.get("macro_vr", []))
        emotion_value = extract_first_element(data.get("emotion", []))
        language = extract_first_element(data.get("language", []))
        speech_value = extract_first_element(data.get("speech", []))
        head = extract_first_element(data.get("head", []))
        gesture = extract_first_element(data.get("gesture", []))
        wait = extract_first_element(data.get("wait", []))
        url = extract_first_element(data.get("url", []))
        message = extract_first_element(data.get("message", "N/A"))

        rospy.loginfo("Status: %s" % status)
        rospy.loginfo("Msg: %s" % msg_field)
        rospy.loginfo("Error: %s" % error)
        rospy.loginfo("Action: %s" % action)
        rospy.loginfo("Macro VR: %s" % macro_vr)
        rospy.loginfo("Emotion: %s" % emotion_value)
        rospy.loginfo("Language: %s" % language)
        rospy.loginfo("Speech: %s" % speech_value)
        rospy.loginfo("Head: %s" % head)
        rospy.loginfo("Gesture: %s" % gesture)
        rospy.loginfo("Wait: %s" % wait)
        rospy.loginfo("URL: %s" % url)
        rospy.loginfo("Message: %s" % message)

        # Se vuoi eseguire funzioni per modificare lo stato del robot:
        emotion(emotion_value)
        setlanguage(language)
        nspeech(speech_value)
        
    except json.JSONDecodeError:
        rospy.logerr("Errore nella decodifica del messaggio JSON")



# Sottoscrizione al topic dopo la definizione della funzione callback
gpt_response_sub = rospy.Subscriber(TOPIC_response_gtp, String, callback_gtpresponse)

def emotion(msg):
    print 'social/emotion %s' % (msg)
    emotion_pub.publish(msg)

def nspeech(msg):
    print '/social/speech/to_speak %s' % (msg)
    speech_pub.publish(msg)

def setlanguage(msg):
    print '/social/speech/language %s' % (msg)
    language_pub.publish(msg)

def gpt_request_pub(msg):
    print 'gpt_request_pub %s' % (msg)
    gpt_request_publisher.publish(msg)

##########################
# FUNZIONI PERSONALIZZATE
def key_room():
    emotion("happy")
    say('Ecco la chiave della sua stanza, la prego di prenderla', 'it')
    head_position("left")
    left_shoulder_flexion(20)
    left_shoulder_rotation(20)
    left_elbow(40)
    left_hand(-70)
    emotion("normal")
    wait(4)
    say('Le ricordo che il servizio in camera è dalle 7 alle 9. Se vuole ulteriori informazioni può consultare il sito', 'it')
    wait(9)
    head_position("front")
    gesture("init")

def bot(msg):
    payload = {'query': msg}
    response = requests.get(url=myurl, params=payload)
    content = response.content
    return content

def left(s, n):
    return s[:n]

def gesture(msg):
    gesture_pub.publish(msg)

def reset_face():    
    rospy.loginfo("resetting face")

# def speech(msg, language):
#     say(msg, language)
#     gesture('gesture')

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
    print "Ciao mondo!"

def callback(data):# detect face  
    global tracking
    if data.data == 0 and tracking:
        tracking = False
    elif data.data != 0 and not tracking:
        tracking = True
        speech("ciao")

def command(msg):
    print msg
    t = Thread(target=run_code, args=(msg,))
    t.start()
    return "ok"

def listener():
    mylanguage = "it"
    begin()
    print "Interactive Mode Start"
    reset_face()
    emotion("startblinking")
    gesture("gesture")
    #setlanguage(mylanguage)
    say("Ciao sono martina ",mylanguage)
    say("Apri la applicazione e parla con me",mylanguage)

    # Utilizzo della funzione che gestisce gli errori del socket
   # serverSocket = create_server_socket(SERVER_ADDRESS, SERVER_PORT)

    connectionSocket, clientAddress = serverSocket.accept()
    myloop = True

    while myloop:
        try:
            myrequest = connectionSocket.recv(1024)
        except socket.timeout:
            print "Timeout nella ricezione dei dati"
            continue

        if myrequest:
            print myrequest
            keyword = "martina"
            msglenght = len(myrequest)
            keylenght = len(keyword)
            mycommand = ""
            if left(myrequest.lower(), keylenght) == keyword:
                mycommand = myrequest[keylenght+1:msglenght].lower()

                if mycommand == "descrivi opera":
                    gpt_request_pub('attiva la function Descrivi_opera')

                elif mycommand in ["parla inglese", "speak english", "you speak english"]:
                    mylanguage = "en"
                    speech("i speak english now", mylanguage)

                elif mycommand in ["parla italiano", "speak italian", "you speak italian"]:
                    mylanguage = "it"
                    speech("adesso parlo italiano", mylanguage)

                elif mycommand in ["alza le braccia", "alza le mani", "raise your arms"]:
                    gesture("up")

                elif mycommand in ["saluta", "saluto", "say hello"]:
                    gesture("hello")

                elif mycommand in ["abbassa le braccia", "abassa le mani", "lower your arms"]:
                    gesture("down")

                elif mycommand in ["spengiti", "spegniti", "arresta il sistema"]:
                    os.system("sudo halt")

                elif mycommand == "guarda avanti":
                    pan(0)
                    tilt(0)

                elif mycommand == "voglio cercare un hotel":
                    connectionSocket.send("https://www.booking.com")
                    speech("ti apro il sito di booking.com", mylanguage)

                elif "aiuto" in mycommand or "help" in mycommand:
                    connectionSocket.send("https://social.marrtino.org/setup-robot/interactive-mode")
                    speech("ti apro il sito di marrtino", mylanguage)

                elif "robotica" in mycommand:
                    connectionSocket.send("https://www.robotics-3d.com")
                    speech("ti apro il sito di Robotics 3d", mylanguage)

                elif mycommand == "hotel a firenze" or mycommand == "hotel at florence":
                    connectionSocket.send("https://www.booking.com/searchresults.it.html?ss=firenze")
                    speech("ti apro il sito di Booking per fare la prenotazione", mylanguage)

                elif mycommand == "quiz" or mycommand == "apri il quiz":
                    connectionSocket.send("http://10.3.1.1:8080/quiz/index.html")
                    speech("Adesso proviamo a fare il quiz insieme", mylanguage)

                elif mycommand == "telepresenza" or mycommand == "apri la telepresenza":
                    connectionSocket.send("http://10.3.1.1:8080/social/navigation.php")
                    speech("Adesso puoi farmi camminare da remoto", mylanguage)

            if myrequest == "stop":
                speech("ci vediamo alla prossima", mylanguage)
                myloop = False

            if myrequest == "fine":
                speech("ci vediamo alla prossima", mylanguage)
                myloop = False

            if myrequest == "PING":
                connectionSocket.send("PONG")

            if myrequest and not mycommand:
                connectionSocket.send("STOP")
                answer = bot(myrequest)
                gesture("gesture")
                speech(answer, mylanguage)
                connectionSocket.send("SAY")

    connectionSocket.close()
    end()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((SERVER_ADDRESS, SERVER_PORT))        # Bind to the port
serverSocket.listen(1)

print("Server waiting on (%s, %d)" % (SERVER_ADDRESS, SERVER_PORT))
# Avvio del listener
listener()
