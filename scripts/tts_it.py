# -*- coding: utf-8 -*-
from pydub import AudioSegment
from gtts import gTTS
import os
import time

def adjust_pitch(sound, octaves=0.0):
    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    pitch_changed_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    return pitch_changed_sound.set_frame_rate(44100)

def adjust_speed(sound, speed=1.0):
    new_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return new_sound.set_frame_rate(44100)

def adjust_pitch_and_speed(file_path, octaves=0.0, speed=1.0):
    sound = AudioSegment.from_file(file_path)
    pitch_changed_sound = adjust_pitch(sound, octaves)
    final_sound = adjust_speed(pitch_changed_sound, speed)
    output_file = f'output_with_pitch_{octaves}_and_speed_{speed}.mp3'
    final_sound.export(output_file, format='mp3')
    return output_file

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save('original.mp3')

def main():
    text = input("Enter text to convert to speech: ")
    lang = input("Enter language (e.g., 'it' for Italian, 'en' for English): ")

    # Generate the original audio file from text
    text_to_speech(text, lang)

    # Speed is fixed for this example, but you can also vary it in a similar way if needed
    speed = 1.0

    # Loop through pitch values from -1.0 to 1.0 in steps of 0.2
    for octaves in range(-10, 11, 2):  # This gives -1.0, -0.8, ..., 1.0
        octaves_value = octaves / 10.0
        print(f"Testing pitch: {octaves_value}")
        output_file = adjust_pitch_and_speed('original.mp3', octaves=octaves_value, speed=speed)
        
        # Play the file
        os.system(f'mpg321 {output_file}')
        
        # Delay between playing each pitch variation
        time.sleep(1)

if __name__ == "__main__":
    main()
