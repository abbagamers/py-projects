from selenium import webdriver
#ChromeDriver on Programfiles(x86)
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.fiaformulae.com/")
print(driver.title)
driver.quit()