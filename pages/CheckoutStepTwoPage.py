from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CheckoutStepTwoPage(BasePage):

    url = 'https://www.saucedemo.com/checkout-step-two.html'

    item_added_title = (By.CLASS_NAME, 'inventory_item_name')
    item_added_quantity = (By.CLASS_NAME, 'cart_quantity')

    finish_btn = (By.CSS_SELECTOR, '#finish')

    def get_added_item_title(self):
        item_title = self.driver.find_element(*self.item_added_title)
        return item_title.text

    def get_added_item_quantity(self):
        item_quantity = self.driver.find_element(*self.item_added_quantity)
        return item_quantity.text

    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()

    def quit_driver(self):
        self.driver.quit()
