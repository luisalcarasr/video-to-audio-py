from moviepy.editor import VideoFileClip
import os

input_folder = 'assets'
output_folder = 'out'
# Define the input video file and output audio file
mp4_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

for mp4_file in mp4_files:
  # Load the video clip
  video_clip = VideoFileClip(os.path.join(input_folder, mp4_file))

  # Extract the audio from the video clip
  audio_clip = video_clip.audio

  # Write the audio to a separate file
  audio_clip.write_audiofile(os.path.join(output_folder, mp4_file.replace('.mp4', '.mp3')))

  # Close the video and audio clips
  audio_clip.close()
  video_clip.close()

print("Audio extraction successful!")