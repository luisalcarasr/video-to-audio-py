import os
import json
from datetime import timedelta
import speech_recognition as sr
from pydub import AudioSegment

r = sr.Recognizer()

VIDEOS_DIR = 'assets'
OUTPUT_DIR = 'out'
# Define the input video file and output audio file
videos = [f for f in os.listdir(VIDEOS_DIR) if f.endswith('.mp4')]

for video_name in videos:
    audio_name = video_name.replace('.mp4', '.wav')
    text_name = video_name.replace('.mp4', '.txt')
    json_name = video_name.replace('.mp4', '.json')

    video_segment = AudioSegment.from_file(os.path.join(VIDEOS_DIR, video_name), format="mp4")
    video_segment.export(os.path.join(OUTPUT_DIR, audio_name), format="wav")

    print(f"Audio extraction of {video_name} is done.")

    with sr.AudioFile(os.path.join(OUTPUT_DIR, audio_name)) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        text_file = open(os.path.join(OUTPUT_DIR, text_name), 'w', encoding='utf-8')
        text_file.write(text)
        text_file.close()

    print(f"Transcription of {video_name} is done.")

    audio_segment = AudioSegment.from_file(os.path.join(OUTPUT_DIR, audio_name), format="wav")
    word_timestamp = []
    chunks = len(audio_segment) // 10000
    for i in range(chunks):
        start_time = i * 10000
        end_time = (i + 1) * 10000
        audio_chunk = audio_segment[start_time:end_time]
        audio_chunk_name = audio_name.replace('.wav', f"_{i}.wav")
        audio_chunk.export(os.path.join(OUTPUT_DIR, audio_chunk_name), format="wav")

        with sr.AudioFile(os.path.join(OUTPUT_DIR, audio_chunk_name)) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
            word_timestamp.append({
                'start_time': start_time,
                'end_time': end_time,
                'text': text
            })

        os.remove(os.path.join(OUTPUT_DIR, audio_chunk_name))
    text_file = open(os.path.join(OUTPUT_DIR, json_name), 'w', encoding='utf-8')
    text_file.write(json.dumps({
        'word_timestamp': word_timestamp
    }))

    print(f"Word timestamp of {video_name} is done.")

    # SRT file generation
    srt_name = video_name.replace('.mp4', '.srt')
    srt_file = open(os.path.join(OUTPUT_DIR, srt_name), 'w', encoding='utf-8')

    for i, wt in enumerate(word_timestamp):
        srt_file.write(f"{i + 1}\n0{timedelta(milliseconds=wt['start_time'])},000 --> {timedelta(milliseconds=wt['end_time'])},000\n")
        srt_file.write(f"{wt['text']}\n\n")

    srt_file.close()
    print(f"SRT generation of {video_name} is done.")
