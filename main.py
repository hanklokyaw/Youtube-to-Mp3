import yt_dlp
from pydub import AudioSegment
import os
import pandas as pd

df = pd.read_csv('test_1.csv')

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


# for index, value in df.iterrows():
#     youtube_url = df.loc[index, 'link']
#     download_youtube_as_mp3(youtube_url)

youtube_url = "https://www.bilibili.com/video/BV1Bg4y1r7x4/?spm_id_from=333.999.0.0"
download_youtube_as_mp3(youtube_url)