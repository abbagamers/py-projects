from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#ChromeDriver on Programfiles(x86)
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://fiaformulae.com")
title = driver.title
print(title)
time.sleep(5)
driver.quit()