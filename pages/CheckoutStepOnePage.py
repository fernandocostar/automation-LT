from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CheckoutStepOnePage(BasePage):

    url = 'https://www.saucedemo.com/checkout-step-one.html'

    first_name_field = (By.CSS_SELECTOR, '#first-name')
    last_name_field = (By.CSS_SELECTOR, '#last-name')
    postal_code_field = (By.CSS_SELECTOR, '#postal-code')

    continue_btn = (By.CSS_SELECTOR, '#continue')

    def fill_first_name(self, data):
        first_name_field = self.driver.find_element(*self.first_name_field)
        first_name_field.send_keys(data)

    def fill_last_name(self, data):
        last_name_field = self.driver.find_element(*self.last_name_field)
        last_name_field.send_keys(data)

    def fill_postal_code(self, data):
        postal_code_field = self.driver.find_element(*self.postal_code_field)
        postal_code_field.send_keys(data)

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()

