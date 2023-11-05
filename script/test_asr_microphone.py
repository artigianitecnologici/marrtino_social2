#!/usr/bin/env python3

import asyncio
import websockets
import sys

async def listen(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            print (await websocket.recv())

asyncio.run(listen('ws://10.3.1.1:2700'))
