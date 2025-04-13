import time

from selenium import webdriver
from selenium.webdriver.common.service import Service

# driver = webdriver.Firefox()
# driver = webdriver.Edge()

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)



#If any VPN issue or chrome driver update issue in that time we use this method
# service_obj = Service("Chrome driver path")
# driver = webdriver.Chrome(service_obj)
# driver.get("https://www.google.com/")