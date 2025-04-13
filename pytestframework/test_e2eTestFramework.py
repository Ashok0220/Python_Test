import json

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.login import LoginPage
from page_object.shoppage import ShopPage
from page_object.checkout_confirmation import CheckOut_Confirmation

test_data_path = "C:\\Users\\ashok\\PycharmProjects\\PythonProject\\Data\\test_e2eTestFramework.json"
with open(test_data_path) as file:
    test_data = json.load(file)
    test_list = test_data["data"]

# @pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browser_instance, test_list_item):
    driver = browser_instance
    # driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    # driver.find_element(By.NAME, "password").send_keys("learning")
    # driver.find_element(By.ID, "signInBtn").click()
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    # loginPage.login()
    shoppe = loginPage.login(test_list_item["User_email"], test_list_item["User_password"])
    shoppe.add_product_to_cart(test_list_item["product_name"])
    print(shoppe.getTitle())
    # shoppe.go_to_cart()
    checkout_confirmation = shoppe.go_to_cart()
    print(checkout_confirmation.getTitle())
    checkout_confirmation.check_out_page()
    checkout_confirmation.delivery_address_page("ind")
    checkout_confirmation.validate_order_confirm_message()


    # driver.find_element(By.CSS_SELECTOR, "a[href*='/angularpractice/shop']").click()
    # products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    #
    # for i in products:
    #     mobiles = i.find_element(By.XPATH, "div/h4/a").text
    #     if mobiles == "Blackberry":
    #         i.find_element(By.XPATH, "div/button").click()
    #
    # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    # driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
    # driver.find_element(By.ID, "country").send_keys("ind")
    # wait = WebDriverWait(driver, 10)
    # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    #
    # driver.find_element(By.LINK_TEXT, "India").click()
    # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    #
    # driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    # ordermessage = driver.find_element(By.CLASS_NAME, "alert-success").text
    #
    # print(ordermessage)
    #
    # assert "Success! Thank you!" in ordermessage

