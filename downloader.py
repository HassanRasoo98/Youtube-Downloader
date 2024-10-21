import json
import os
from datetime import datetime
from pytubefix import YouTube

if not os.path.exists('history.json'):
    data = {'history': []}
    with open('history.json', 'w') as f:
        json.dump(data, f, indent=2)

# Function to download video
def download_video(url, output_path='.'):
    yt = YouTube(url)
    # Get the highest resolution video stream
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    print(f"Downloading video: {video_stream.title}")
    video_stream.download(output_path=output_path)
    print(f"Video downloaded at: {output_path}/{video_stream.default_filename}")
    
    with open('history.json', 'r') as f:
        data = json.load(f)

    data['history'].append(
        {
            'title': video_stream.title,
            'type': 'video',
            'link': url,
            'download_time': datetime.now().strftime("%d%m%Y")
        }
    )
    
    with open('history.json', 'w') as f:
        json.dump(data, f, indent=2)

# Function to download audio
def download_audio(url, output_path='.'):
    yt = YouTube(url)
    # Get the audio-only stream
    audio_stream = yt.streams.filter(only_audio=True).first()
    print(f"Downloading audio: {audio_stream.title}")
    name = f"{audio_stream.title}.mp3"
    audio_stream.download(filename=name, output_path=output_path)
    print(f"Audio downloaded at: {output_path}/{name}")

    with open('history.json', 'r') as f:
        data = json.load(f)

    data['history'].append(
        {
            'title': audio_stream.title,
            'type': 'audio',
            'link': url,
            'download_time': datetime.now().strftime("%d-%m-%Y")
        }
    )
    
    with open('history.json', 'w') as f:
        json.dump(data, f, indent=2)

# Example usage
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=VGPmFSB8qVY&feature=youtu.be"
    # download_video(video_url, output_path='videos')  # Change output_path as needed
    download_audio(video_url, output_path='audio')   # Change output_path as needed
