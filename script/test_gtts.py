from gtts import gTTS
#import pygame
import tempfile
import os

# Text to convert to speech
text = "Ciao , sono marrtina e sono un robot sociale"

# Create gTTS object
tts = gTTS(text,lang='it')

# Save gTTS output to a temporary file
temp_file =  "/tmp/cache.mp3"
tts.save(temp_file)


os.system("play "+ temp_file+" -q pitch 500 tempo 1.1")
#os.remove(temp_file)

