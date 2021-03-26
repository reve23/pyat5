from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/")
print(f"This is title {driver.title}")

search = driver.find_element_by_name("s")
search.send_keys("java")
search.submit()

time.sleep(6)
driver.quit()
