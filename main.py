import streamlit as st
import os
from pathlib import Path
import time

from downloader import *

# Streamlit frontend
st.title("YouTube Video/Audio Downloader")

# Input field for YouTube video URL
url = st.text_input("Enter the YouTube video URL:")

# Output directory (using Streamlit's temporary directory)
output_path = "downloads"
Path(output_path).mkdir(parents=True, exist_ok=True)

# Buttons to download video or audio
if st.button("Download Video"):
    if url:
        with st.spinner("Downloading video..."):
            try:
                video_file = download_video(url, output_path=output_path)
                st.success(f"Video downloaded successfully!")
                st.video(video_file)  # Show video in Streamlit
                
                # Clean up: remove video after showing it
                time.sleep(3)  # Give a delay to allow user to see the video
                if os.path.exists(video_file):
                    os.remove(video_file)
                    st.info(f"Video file removed from server.")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please enter a valid URL.")

if st.button("Download Audio"):
    if url:
        with st.spinner("Downloading audio..."):
            try:
                audio_file = download_audio(url, output_path=output_path)
                st.success(f"Audio downloaded successfully!")
                
                # Provide download link for audio
                generate_download_link(audio_file)
                
                # Optionally remove the audio file after download, or keep it for a while
                time.sleep(60)  # Wait for 1 minute before removing
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                    st.info(f"Audio file removed from server.")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please enter a valid URL.")
