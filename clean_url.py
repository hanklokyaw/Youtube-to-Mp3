import pandas as pd
from urllib.parse import urlparse, parse_qs

# Load your CSV
csv_file = "cantonese_songs.csv"  # Update if needed
df = pd.read_csv(csv_file, encoding="utf-8-sig")


def clean_youtube_url(url):
    """
    Extract just the main video link (https://www.youtube.com/watch?v=VIDEO_ID)
    from a URL that might contain extra query parameters.
    """
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    # Get the video ID (v) parameter
    video_id = query.get('v', [None])[0]

    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        # If there's no 'v' parameter, return the original URL or handle as needed
        return url


# Apply the cleaning function to each URL in the 'URL' column
df['Clean_URL'] = df['URL'].apply(clean_youtube_url)

# Save the cleaned URLs to a new CSV
output_csv = "cantonese_songs_cleaned.csv"
df.to_csv(output_csv, index=False, encoding="utf-8-sig")
print(f"✅ Cleaned URLs saved to {output_csv}")
