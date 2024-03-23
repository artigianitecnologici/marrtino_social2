#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import json
import asyncio
import websockets
import sys
import threading
import requests
import time
import socket               # Import socket module
import os
import random

from threading import Thread

SERVER_ADDRESS = '10.3.1.1'             # Get local machine name
SERVER_PORT = 9000      

TOPIC_asr = "/social/asr"

rospy.init_node("node_asr")
# Publisher
pubAsr = rospy.Publisher(TOPIC_asr, String, queue_size=10)

def timerping():
  threading.Timer(10.0, timerping).start()
  print("Ciao mondo!")


def listener():
    mylanguage = "it"
    print("Interactive Node Asr for App start")
    connectionSocket, clientAddress = serverSocket.accept()
    myrequest = ""
    myloop=True
    count = 0
    #
    while myloop==True:
        # recv can throw socket.timeout
        #connectionSocket.settimeout(5.0)
       
        try:
            myrequest =  connectionSocket.recv(1024)
            myrequest =  myrequest.decode("utf-8")
            
        except socket.timeout: # fail after 1 second of no activity
            print("Didn't receive data! [Timeout]")
        #finally:
            #s.close()
        if myrequest=="PING":
            #connectionSocket.send("PONG")
            myrequest=""
        
        if (myrequest != ""):
            rospy.loginfo(myrequest)
            pubAsr.publish(myrequest)

        

    print("Close connection on %d" % SERVER_PORT)
    connectionSocket.close()


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((SERVER_ADDRESS, SERVER_PORT))        # Bind to the port
serverSocket.listen(1)

print("Server waiting on (%s, %d)" % (SERVER_ADDRESS, SERVER_PORT))

listener()
