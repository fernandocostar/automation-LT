from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import EXPLICITLY_WAIT_TIME_DEFAULT


class Page:

    def __init__(self, driver, explicitly_wait=None):
        self.driver = driver
        self.explicitly_wait = EXPLICITLY_WAIT_TIME_DEFAULT if not explicitly_wait else explicitly_wait

    def go_to(self):
        self.driver.get(self.url)

    def get_page_loaded_url(self):
        WebDriverWait(self.driver, self.explicitly_wait).until(EC.url_changes(self.url))
        return self.driver.current_url

    def get_url(self):
        return self.url

    def quit_driver(self):
        self.driver.quit()
