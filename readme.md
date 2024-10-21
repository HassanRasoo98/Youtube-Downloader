# YouTube Video/Audio Downloader

This Streamlit app allows users to download YouTube videos and audio directly from a provided YouTube URL. The app stores the downloaded videos and audios in the video and audio folders respectively. These folders are automatically generated from the code.

## Features
- Download YouTube videos in the highest available resolution.
- Download audio-only from YouTube videos.

## Steps to Run the App

1. **Clone the repository**:
    You need to have git installed on your system to run this command. Otherwise you can download the project folder as zip folder and skip this step.
   ```bash
   git clone https://github.com/HassanRasoo98/Youtube-Downloader
   cd Youtube-Downloader
   ```

2. **Install the dependencies**:
   Make sure you have Python installed. Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   After installing the dependencies, start the app using Streamlit:
   ```bash
   streamlit run main.py
   ```

4. **Access the app**:
   Once the app is running, it will provide a local URL (e.g., `http://localhost:8501`). Open the provided URL in your browser to access the app.

## How to Use the App

1. **Enter a YouTube URL**:
   - In the input field, paste the URL of the YouTube video you want to download.

2. **Download Video**:
   - Click the "Download Video" button to download the highest resolution version of the video.

3. **Download Audio**:
   - Click the "Download Audio" button to download the audio-only version of the video.

### Example:
1. Paste a YouTube URL such as `https://www.youtube.com/watch?v=dQw4w9WgXcQ`.
2. Choose whether to download the video or audio.
3. Click the download button to save the file locally.

## Dependencies
- Python 3.7+
- Streamlit
- pytube
