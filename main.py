import traceback
import streamlit as st
from pathlib import Path

from downloader import *

# Streamlit frontend
st.title("YouTube Video/Audio Downloader")

# Input field for YouTube video URL
url = st.text_input("Enter the YouTube video URL:")

# Output directory (using Streamlit's temporary directory)
video_path = "video"
audio_path = "audio"
Path(video_path).mkdir(parents=True, exist_ok=True)
Path(audio_path).mkdir(parents=True, exist_ok=True)

# Buttons to download video or audio
if st.button("Download Video"):
    if url:
        with st.spinner("Downloading video..."):
            try:
                video_file = download_video(url, output_path=video_path)
                st.success(f"Video downloaded successfully!")
                
            except Exception as e:
                traceback.print_exc()
                st.error(f"Error: {e}")
    else:
        st.error("Please enter a valid URL.")

if st.button("Download Audio"):
    if url:
        with st.spinner("Downloading audio..."):
            try:
                audio_file = download_audio(url, output_path=audio_path)
                st.success(f"Audio downloaded successfully!")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please enter a valid URL.")
