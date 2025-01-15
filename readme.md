# YouTube Video/Audio Downloader

This application allows users to download YouTube videos directly from a provided YouTube URL. The app stores the downloaded videos in the `video` folder. This folder are automatically generated from the code.

## Features
- Download YouTube videos in the highest available resolution.

## Steps to Run the App

1. **Clone the repository**:
    You need to have git installed on your system to run this command. Otherwise, you can download the project folder as a zip folder and skip this step.
   ```bash
   git clone https://github.com/HassanRasoo98/Youtube-Downloader.git
   cd Youtube-Downloader
   ```

2. **Install the dependencies**:
   Make sure you have Python installed. Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   After installing the dependencies, you can run the application using the following command:
   ```bash
   python main.py <YouTube-URL>
   ```

   - Replace `<YouTube-URL>` with the actual URL of the YouTube video you want to download.

4. **Access the downloaded files**:
   - The downloaded videos will be saved in the `videos` folder.

## How to Use the App

1. **Enter a YouTube URL**:
   - Provide the URL of the YouTube video you want to download as a command-line argument.

2. **Download Video**:
   - Run the command to download the highest resolution version of the video.

### Example:
1. To download a video:
   ```bash
   python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

## Dependencies
- Python 3.7+
- yt-dlp