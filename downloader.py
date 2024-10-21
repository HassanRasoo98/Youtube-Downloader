import os
import streamlit as st
from pytubefix import YouTube

# Function to download video
def download_video(url, output_path='.'):
    yt = YouTube(url)
    # Get the highest resolution video stream
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    print(f"Downloading video: {video_stream.title}")
    video_stream.download(output_path=output_path)
    print(f"Video downloaded at: {output_path}/{video_stream.default_filename}")

# Function to download audio
def download_audio(url, output_path='.'):
    yt = YouTube(url)
    # Get the audio-only stream
    audio_stream = yt.streams.filter(only_audio=True).first()
    print(f"Downloading audio: {audio_stream.title}")
    audio_stream.download(output_path=output_path)
    print(f"Audio downloaded at: {output_path}/{audio_stream.default_filename}")
    
# Function to generate a download link
def generate_download_link(file_path):
    file_name = os.path.basename(file_path)
    with open(file_path, "rb") as file:
        btn = st.download_button(
            label=f"Download {file_name}",
            data=file,
            file_name=file_name,
            mime='application/octet-stream'
        )
    return btn


# Example usage
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=VGPmFSB8qVY&feature=youtu.be"
    # download_video(video_url, output_path='videos')  # Change output_path as needed
    download_audio(video_url, output_path='audio')   # Change output_path as needed
