from gtts import gTTS
#import pygame
import tempfile
import os

# Text to convert to speech
text = "Ciao , io mi chiamo martina"

# Create gTTS object
tts = gTTS(text,lang='it')

# Save gTTS output to a temporary file
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
temp_file_path = temp_file.name
tts.save(temp_file_path)
temp_file.close()

os.system("play "+ temp_file_path+" -q pitch 200 tempo 1")
os.remove(temp_file_path)

# Clean up the temporary file
os.remove(temp_file_path)
