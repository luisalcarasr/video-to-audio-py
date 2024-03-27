from moviepy.editor import VideoFileClip
import os
import speech_recognition as sr
from pydub import AudioSegment

r = sr.Recognizer()

input_folder = 'assets'
output_folder = 'out'
# Define the input video file and output audio file
mp4_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

for mp4_file in mp4_files:
    audio = AudioSegment.from_file(os.path.join(input_folder, mp4_file), format="mp4")
    audio.export(os.path.join(output_folder, mp4_file.replace('.mp4', '.wav')), format="wav")

audio_files = [f for f in os.listdir(output_folder) if f.endswith('.wav')]

for file in audio_files:
    with sr.AudioFile(os.path.join(output_folder, file)) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        text_file = open(os.path.join(output_folder, file.replace('.wav', '.txt')), 'w', encoding='utf-8')
        text_file.write(text)
        text_file.close()
