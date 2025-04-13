import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")
driver.maximize_window()
driver.implicitly_wait(2)

driver.switch_to.frame("frame1")

testx = driver.find_element(By.ID, "sampleHeading").text
print(testx)

driver.switch_to.default_content()

driver.switch_to.frame("frame2")
test2 = driver.find_element(By.ID, "sampleHeading").text
print(test2)

driver.switch_to.default_content()