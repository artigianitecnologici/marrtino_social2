#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import sys
import json

'''This script processes audio input from the microphone and displays the transcribed text.'''

TOPIC_asr = "/social/asr"
rospy.init_node("node_asr")
# Publisher
pubAsr = rospy.Publisher(TOPIC_asr, String, queue_size=10)

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text
    
# list all audio devices known to your system
print("Display input/output devices")
print(sd.query_devices())


# get the samplerate - this is needed by the Kaldi recognizer
device_info = sd.query_devices(sd.default.device[0], 'input')
samplerate = int(device_info['default_samplerate'])

# display the default input device
print("===> Initial Default Device Number:{} Description: {}".format(sd.default.device[0], device_info))

# setup queue and callback function
q = queue.Queue()

def recordCallback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))
    
# build the model and recognizer objects.
print("===> Build the model and recognizer objects.  This will take a few minutes.")

model = Model(model_name="vosk-model-it-0.22")
recognizer = KaldiRecognizer(model, samplerate)
recognizer.SetWords(False)

print("===> Begin recording. Press Ctrl+C to stop the recording ")
try:
    with sd.RawInputStream( device=1,
            dtype="int16", channels=1, callback=recordCallback):
        while True:
            data = q.get()        
            if recognizer.AcceptWaveform(data):
                recognizerResult = recognizer.Result()
                # convert the recognizerResult string into a dictionary  
                resultDict = json.loads(recognizerResult)
                if not resultDict.get("text", "") == "":
                    myasr = resultDict["text"]
                    rospy.loginfo(myasr)
                    pubAsr.publish(myasr)
                #else:
                    #print("no input sound")

except KeyboardInterrupt:
    print('===> Finished Recording')
except Exception as e:
    print(str(e))
