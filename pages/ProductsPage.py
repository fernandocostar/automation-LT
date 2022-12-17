import random

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductsPage(BasePage):

    url = 'https://www.saucedemo.com/inventory.html'

    cart_badge = (By.CSS_SELECTOR, '#shopping_cart_container > a > span')

    inventory_list = (By.CLASS_NAME, 'inventory_list')
    list_items = (By.CLASS_NAME, 'inventory_item')

    item_add_button = (By.CSS_SELECTOR, 'button')
    item_title = (By.CLASS_NAME, 'inventory_item_name')

    def add_random_item_to_cart(self):

        inventory_list = self.driver.find_element(*self.inventory_list)
        items = inventory_list.find_elements(*self.list_items)
        selected_item = random.choice(items)

        item_title = selected_item.find_element(*self.item_title)
        item_btn = selected_item.find_element(*self.item_add_button)

        item_btn.click()

        assert self.driver.find_element(*self.cart_badge).text == '1'

        return item_title.text

