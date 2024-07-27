import yt_dlp
from pydub import AudioSegment
import os

def download_youtube_as_mp3(url, output_path='output'):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        title = info_dict.get('title', None)
        print(f"{title} has been successfully downloaded and converted to MP3.")

# Example usage
youtube_url = 'https://www.youtube.com/watch?v=yWnFkrtBwYE&list=RDMMCjIEYEOX2FQ'
download_youtube_as_mp3(youtube_url)
