import os
import sys
import yt_dlp

url = sys.argv[1]
os.makedirs('audio', exist_ok=True)

def download_audio(audio_url, output_path='audio'):
    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '0'}],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s'
    }
    # with yt_dlp.YoutubeDL(f"{output_path}/{ydl_opts}") as ydl:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([audio_url])

if __name__ == '__main__':

    if not url:
        print("Please Provide Valid url in argument!")
        exit(0)

    try:
        download_audio(url)
    except Exception as e:
        print(f"Error: {e}")

