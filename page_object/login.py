from selenium.webdriver.common.by import By

from Utilsfiles.browserutil import BrowserUtils
from page_object.shoppage import ShopPage


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.User_name = (By.ID, "username")
        self.user_password = (By.NAME, "password")
        self.Sign_btn = (By.ID, "signInBtn")


    def login(self, Username, Password):
        self.driver.find_element(*self.User_name).send_keys(Username)
        self.driver.find_element(*self.user_password).send_keys(Password)
        self.driver.find_element(*self.Sign_btn).click()
        shoppe = ShopPage(self.driver)
        return  shoppe

