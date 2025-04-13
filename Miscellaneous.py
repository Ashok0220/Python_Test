import time
from locale import windows_locale

from selenium import webdriver
from selenium.webdriver.common.by import By

# headless browser
driver1 = webdriver.ChromeOptions()
driver1.add_argument("headless")

# Avoid certificate errors
driver1.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=driver1)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(2)



# Scroll down to bottom
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

# Scroll to particular mid on page
# driver.execute_script("window.scrollTo(0, 1000);")

# Screen shot
driver.get_screenshot_as_file("headless.png")


time.sleep(2)