import yt_dlp
import os
import pandas as pd

# Read cleaned CSV with video URLs
csv_file = "cantonese_songs_cleaned.csv"
df = pd.read_csv(csv_file, encoding="utf-8-sig")

# Ensure the output folder exists
output_folder = "output/cantonese_songs"
os.makedirs(output_folder, exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',  # or try 'bestaudio'
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    # Let yt-dlp fetch cookies from your browser (Chrome in this case)
    'cookies-from-browser': 'chrome',
    # Optional: Set a common User-Agent to mimic a real browser
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/132.0.0.0 Safari/537.36'
    }
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for _, row in df.iterrows():
        url = row['Clean_URL']
        print(f"Downloading: {url}")
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Error downloading {url}: {e}")

print("All download attempts finished!")
