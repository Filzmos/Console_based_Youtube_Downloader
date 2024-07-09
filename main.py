#python -m pip install yt-dlp
#ffmpeg auch notwendig, https://www.youtube.com/watch?v=JR36oH35Fgg
from yt_dlp import YoutubeDL

def download(video_url, save_path):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'no-mtime': True  # Verhindert die Änderung des Datei-Zeitstempels
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f'Successfully downloaded video to {save_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    video_url = input("Video URL: ")
    save_path = input("Where should the video be saved: ")
    download(video_url, save_path)