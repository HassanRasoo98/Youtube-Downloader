import sys
import yt_dlp

url = sys.argv[1]

def download_video(video_url, output_path='videos'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == '__main__':

    if not url:
        print("Please Provide Valid url in argument!")
        exit(0)

    try:
        download_video(url)
    except Exception as e:
        print(f"Error: {e}")



