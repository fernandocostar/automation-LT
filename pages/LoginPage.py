from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import EXPLICITLY_WAIT_TIME_DEFAULT


class LoginPage:

    url = 'https://www.saucedemo.com/'

    username_field = (By.CSS_SELECTOR, '#user-name')
    password_field = (By.CSS_SELECTOR, '#password')

    login_btn = (By.CSS_SELECTOR, '#login-button')

    def __init__(self, driver, explicitly_wait=None):
        self.driver = driver
        self.explicitly_wait = EXPLICITLY_WAIT_TIME_DEFAULT if not explicitly_wait else explicitly_wait

    def go_to(self):
        self.driver.get(self.url)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()
    
    def fill_username(self, data):
        username_field = self.driver.find_element(*self.username_field)
        username_field.send_keys(data)

    def fill_password(self, data):
        password_field = self.driver.find_element(*self.password_field)
        password_field.send_keys(data)

    def get_page_loaded_url(self):
        WebDriverWait(self.driver, self.explicitly_wait).until(EC.url_changes(self.url))
        return self.driver.current_url

    def quit_driver(self):
        self.driver.quit()
