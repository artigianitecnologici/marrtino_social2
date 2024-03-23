#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import json
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
            resultDict = json.loads(myasr)
            asrtext = resultDict.get("text", "")
            if (not asrtext == ""):
                rospy.loginfo(asrtext)
                pubAsr.publish(asrtext)

asyncio.run(listen('ws://127.0.0.1:2700'))
