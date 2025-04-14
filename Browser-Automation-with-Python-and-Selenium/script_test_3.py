import time

from selenium import webdriver

# Helps with recording, not required
opts = webdriver.ChromeOptions()
opts.add_argument('--disable-gpu')

# create a new browser from Chrome options
browser1 = webdriver.Chrome(options=opts)

# browser interactions and execute scripts
# open the page web with the URL
URL = 'https://techstepacademy.com/training-ground'
browser1.get(URL)
print("page opened with browser: " + browser1.name)

# use javascript to open a new tab with the URL of page web
browser1.execute_script("window.open('https://techstepacademy.com/training-ground', '_blank');")

# wait for 3 seconds to see the new tab opened
time.sleep(3)
print("new tab opened with browser: " + browser1.name)
