from selenium.webdriver.common.by import By

from pages.Page import Page


class BasePage(Page):

    page_title = (By.CLASS_NAME, 'title')

    def get_page_title(self):
        page_title = self.driver.find_element(*self.page_title)
        return page_title.text

