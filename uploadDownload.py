from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver1 = webdriver.ChromeOptions()
driver1.add_argument("headless")
fruits_name = "Apple"
filepath = "C:\\Users\\ashok\\Downloads"
driver = webdriver.Chrome(options=driver1)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, "downloadButton").click()



fileinputbtn = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
fileinputbtn.send_keys(filepath)

# wait = WebDriverWait(driver, 20)
# tes = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
# wait.until(expected_conditions.visibility_of_element_located(tes))
# print(driver.find_element(*tes).text)

pricecolum = driver.find_element(By.XPATH, "//div[(text())='Price']").get_attribute("data-column-id")
actualprice = driver.find_element(By.XPATH, "//div[text()='"+fruits_name+"']/parent::div/parent::div/div[@id='cell-"+pricecolum+"-undefined']").text

print(actualprice)