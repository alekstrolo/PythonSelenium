from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://chromedriver.chromium.org/downloads")
driver.fullscreen_window()
time.sleep(10)
print(driver.current_url)

driver.back()
driver.forward()

inputField = driver.find_element(By.NAME, "q")

inputField.send_keys("Wyszukaj mnie")

time.sleep(10)
searchButton = driver.find_element(By.ID, "sites-searchbox-search-button")
searchButton.click()
time.sleep(10)
driver.close()
driver.quit()