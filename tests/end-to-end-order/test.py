import unittest

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import LoginPage, ProductsPage
from config.config import IMPLICITLY_WAIT_TIME_DEFAULT, WEBDRIVER_PATH

driver = webdriver.Chrome(WEBDRIVER_PATH)
driver.maximize_window()
driver.implicitly_wait(IMPLICITLY_WAIT_TIME_DEFAULT)

login_page = LoginPage.LoginPage(driver)
products_page = ProductsPage.ProductsPage(driver)

login_page.go_to()
login_page.fill_username('standard_user')
login_page.fill_password('secret_sauce')
login_page.click_login()

assert login_page.get_page_loaded_url(), 'https://www.saucedemo.com/inventory.html'

print(products_page.add_random_item_to_cart())

sleep(10)