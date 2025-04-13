from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilsfiles.browserutil import BrowserUtils
from demoTest import driver
class CheckOut_Confirmation(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.check_out_btn = (By.XPATH, "//button[@class='btn btn-success']")
        self.check_out_btn = (By.XPATH, "//*[contains(text(),'Checkout')]")
        self.country_input = (By.ID, "country")
        self.country_options = (By.LINK_TEXT, "India")
        self.checkbox_option = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_btn = (By.CSS_SELECTOR, "input[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")

    def check_out_page(self):
        driver.implicitly_wait(3)
        self.driver.find_element(*self.check_out_btn).click()

    def delivery_address_page(self, Countryname):
        self.driver.find_element(*self.country_input).send_keys(Countryname)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_options))
        self.driver.find_element(*self.country_options).click()
        self.driver.find_element(*self.checkbox_option).click()
        self.driver.find_element(*self.submit_btn).click()

    def validate_order_confirm_message(self):
        ordermessage = self.driver.find_element(*self.success_message).text
        print(ordermessage)
        assert "Success! Thank you!" in ordermessage



