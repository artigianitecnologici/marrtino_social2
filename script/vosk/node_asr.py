#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

import asyncio
import websockets
import sys


TOPIC_asr = "/social/asr"
rospy.init_node("node_asr")
# Publisher
pubAsr = rospy.Publisher(TOPIC_asr, String, queue_size=10)

async def listen(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            myasr = (await websocket.recv())
            rospy.loginfo(myasr)
            pubAsr.publish(myasr)

asyncio.run(listen('ws://10.3.1.1:2700'))
