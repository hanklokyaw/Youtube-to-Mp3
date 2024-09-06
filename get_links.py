# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import pandas as pd
#
# # Set up the WebDriver (make sure the path to your chromedriver is correct)
# service = Service("C:/Users/hboyz/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  # Replace with the correct path to your ChromeDriver
# driver = webdriver.Chrome(service=service)
#
# # Open the webpage
# driver.get("https://space.bilibili.com/3546743952116225/favlist?fid=3320705225")
#
# # Give the page some time to load dynamically loaded content (adjust if necessary)
# driver.implicitly_wait(10)
#
# # Find all 'a' tags with href attribute starting with '//www.bilibili.com/video/'
# links = driver.find_elements(By.XPATH, '//a[starts-with(@href, "//www.bilibili.com/video/")]')
#
# # Extract the href attribute and add "https:" at the beginning
# video_links = [link.get_attribute('href') for link in links]
#
# # Create a DataFrame
# df = pd.DataFrame(video_links, columns=['link'])
#
# # Add an index column
# df.reset_index(inplace=True)
#
# # Print the DataFrame
# print(df)
# df.to_csv("test.csv")
#
# # Close the browser
# driver.quit()


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Initialize the Firefox WebDriver
service = Service()  # Ensure geckodriver is in your PATH
driver = webdriver.Firefox(service=service)

# Open the initial page
url = "https://space.bilibili.com/3546743952116225/favlist?spm_id_from=333.880.0.0"
driver.get(url)

# Initialize list to store video links
video_links = []


# Function to extract video links from the current page
def extract_video_links():
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for a in soup.find_all('a', href=True):
        if a['href'].startswith("//www.bilibili.com/video/"):
            video_links.append('https:' + a['href'])


# Extract links from the first page
extract_video_links()

# Example loop to handle multiple pages
# Adjust the number of pages or conditions as needed
for i in range(3):  # Change this range according to the number of pages you want to scrape
    try:
        # Wait for the "Next" button to be clickable
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="page-fav"]/div[1]/div[2]/div[3]/ul[2]/li[6]'))
        )
        # Click the "Next" button
        next_button.click()

        # Wait for new content to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//ul[contains(@class, "fav-video-list")]'))
        )

        # Extract links from the new page
        extract_video_links()

    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Create a DataFrame
df = pd.DataFrame(video_links, columns=['link'])

# Add an index
df.index.name = 'index'

# Close the browser
driver.quit()

# Print or save the DataFrame
print(df)
df.to_csv("test_1.csv")
