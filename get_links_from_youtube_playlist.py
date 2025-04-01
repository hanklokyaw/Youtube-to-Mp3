from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Automatically download and manage ChromeDriver
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

# Open the YouTube playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLpTw4YCghfSJbJAgQZW9qStk5rNVVyz-i"  # Replace with your playlist URL
driver.get(playlist_url)

# Give time for dynamic elements to load
time.sleep(5)

# Scroll to the bottom to load all videos
scroll_pause_time = 2  # Adjust if necessary
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find all video links in the playlist
video_elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/watch?")]')

# Extract URLs and titles
video_links = []
for video in video_elements:
    url = video.get_attribute("href")
    title = video.get_attribute("title")
    if url and title:  # Avoid None values
        video_links.append((title, url))

# Create a DataFrame
df = pd.DataFrame(video_links, columns=['Title', 'URL'])

# Save to CSV
df.to_csv("cantonese_songs.csv", index=False, encoding="utf-8-sig")

print("✅ CSV file saved: youtube_playlist_songs.csv")

# Close the browser
driver.quit()
