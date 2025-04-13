from selenium.webdriver.common.by import By

from Utilsfiles.browserutil import BrowserUtils
from demoTest import driver
from page_object.checkout_confirmation import CheckOut_Confirmation


class ShopPage(BrowserUtils):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='/angularpractice/shop']")
        self.Products_list = (By.XPATH, "//div[@class='card h-100']")
        self.cart_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_product_to_cart(self, productsname):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.Products_list)
        for i in products:
            mobiles = i.find_element(By.XPATH, "div/h4/a").text
            if mobiles == productsname:
                i.find_element(By.XPATH, "div/button").click()


    def go_to_cart(self):
        driver.implicitly_wait(4)
        self.driver.find_element(*self.cart_btn).click()
        checkout = CheckOut_Confirmation(self.driver)
        return checkout

