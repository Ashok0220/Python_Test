import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

# driver = webdriver.Firefox()
# driver = webdriver.Edge()

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


name = "Ashok"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
# driver.find_element(By.ID, "alertbtn").click()
driver.find_element(By.ID, "confirmbtn").click()

alret = driver.switch_to.alert
alretext = alret.text
print(alretext)

# alret.accept()
alret.dismiss()
time.sleep(2)
