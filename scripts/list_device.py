#!/usr/bin/env python3

import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import sys
import json

'''This script processes audio input from the microphone and displays the transcribed text.'''
    
# list all audio devices known to your system
print("Display input/output devices")
print(sd.query_devices())


# get the samplerate - this is needed by the Kaldi recognizer
device_info = sd.query_devices(sd.default.device[0], 'input')
samplerate = int(device_info['default_samplerate'])

# display the default input device
print("===> Initial Default Device Number:{} Description: {}".format(sd.default.device[0], device_info))
