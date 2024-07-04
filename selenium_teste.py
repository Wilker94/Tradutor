from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage
driver.get("https://elevenlabs.io/app/speech-synthesis")

# Wait for the element to load (adjust the wait time as needed)
driver.implicitly_wait(10)

# Click the button to reveal the dropdown menu
button = driver.find_element(By.CSS_SELECTOR, "#content > div.relative.flex-1.min-h-0 > div > div > div.w-full.max-w-[105rem].mx-auto.hstack.flex-1 > div > div.hstack.gap-2.items-center.p-4 > div.w-48 > button")
button.click()

# Find and print all the voice names
voice_names = driver.find_elements(By.CSS_SELECTOR, ".group.h-full.w-full.hstack.items-center.gap-2.flex-1.min-w-0 .text-sm.truncate")
for voice in voice_names:
    print(voice.text)

# Close the WebDriver
driver.quit()
