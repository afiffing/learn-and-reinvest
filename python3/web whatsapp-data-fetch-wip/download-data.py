import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# Setup LibreWolf (Firefox) WebDriver
options = Options()
options.binary_location = "/Applications/LibreWolf.app/Contents/MacOS/librewolf"  # Adjust this path to your LibreWolf binary location
options.add_argument("--user-data-dir='~/Library/Application Support/LibreWolf/Profiles/'")  # Persistent session for WhatsApp Web login

# Initialize WebDriver for LibreWolf (based on Firefox)
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for the QR code to be scanned
# This path should be last div just above "Archived" text.

print("Please scan the QR code to log in...")
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[3]/div/div[3]/button/div/div[2]/div/div")))


# Access the Archived Chats
# This path should be last div class just above "Archived" clea

archived_section = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div [@class='_ak8q']"))
)
archived_section.click()

# Wait for the archived chats to load
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div [@id='app']"))
)

# Function to download media files (images, videos)
def download_media(media_url, media_type):
    try:
        # Get media extension based on type
        file_extension = media_url.split('.')[-1]
        file_name = f"media_file_{int(time.time())}.{file_extension}"

        # Send GET request to download the file
        response = requests.get(media_url, stream=True)

        if response.status_code == 200:
            # Ensure the media directory exists
            if not os.path.exists('media'):
                os.makedirs('media')

            # Write the content to a file
            with open(f"media/{file_name}", 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)

            print(f"{media_type.capitalize()} downloaded: {file_name}")
        else:
            print(f"Failed to download {media_type}. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error downloading {media_type}: {e}")

# Select the archived chat you want to scrape (change this based on the group name you want)
group_name = "D2 22nd Feb to 25th Feb"
group = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, f"//span[@title='{group_name}']"))
)
group.click()

# Wait for the chat to load
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div [@class='x10l6tqk xh8yej3 x1g42fcv']"))
)

# Find media elements (images, videos)
media_elements = driver.find_elements(By.XPATH, "//div [@class='x10l6tqk xh8yej3 x1g42fcv']")

for media in media_elements:
    try:
        # Check if the media is an image or a video
        img_elements = media.find_elements(By.TAG_NAME, 'img')
        video_elements = media.find_elements(By.TAG_NAME, 'video')

        if img_elements:
            # Media is an image
            media_url = img_elements[0].get_attribute("src")
            download_media(media_url, 'image')

        elif video_elements:
            # Media is a video
            media_url = video_elements[0].get_attribute("src")
            download_media(media_url, 'video')

    except Exception as e:
        print(f"Error extracting media: {e}")

# # Close the WebDriver
# driver.quit()
