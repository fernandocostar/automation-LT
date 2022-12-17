from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CartPage(BasePage):

    url = 'https://www.saucedemo.com/cart.html'

    item_added_title = (By.CLASS_NAME, 'inventory_item_name')
    item_added_quantity = (By.CLASS_NAME, 'cart_quantity')

    checkout_btn = (By.CSS_SELECTOR, '#checkout')

    def get_added_item_title(self):
        item_title = self.driver.find_element(*self.item_added_title)
        return item_title.text

    def get_added_item_quantity(self):
        item_quantity = self.driver.find_element(*self.item_added_quantity)
        return item_quantity.text

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()
