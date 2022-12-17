import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages import LoginPage, ProductsPage, CartPage, CheckoutStepOnePage, CheckoutStepTwoPage, CheckoutCompletePage
from config.config import IMPLICITLY_WAIT_TIME_DEFAULT, WEBDRIVER_PATH, HEADLESS_DEFAULT


class OrderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        options = Options()
        if HEADLESS_DEFAULT:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

        cls.driver = webdriver.Chrome(WEBDRIVER_PATH, chrome_options=options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT_TIME_DEFAULT)

        cls.login_page = LoginPage.LoginPage(cls.driver)
        cls.products_page = ProductsPage.ProductsPage(cls.driver)
        cls.cart_page = CartPage.CartPage(cls.driver)
        cls.checkout_step_one_page = CheckoutStepOnePage.CheckoutStepOnePage(cls.driver)
        cls.checkout_step_two_page = CheckoutStepTwoPage.CheckoutStepTwoPage(cls.driver)
        cls.checkout_complete_page = CheckoutCompletePage.CheckoutCompletePage(cls.driver)

    def test_step_1(self):

        self.login_page.go_to()
        self.login_page.fill_username('standard_user')
        self.login_page.fill_password('secret_sauce')
        self.login_page.click_login()

        assert self.login_page.get_page_loaded_url() == self.products_page.get_url()

    def test_step_2(self):
        self.__class__.choosen_item_title = self.products_page.add_random_item_to_cart()
        assert self.__class__.choosen_item_title is not None

    def test_step_3(self):

        self.cart_page.go_to()

        assert self.cart_page.get_added_item_title() == self.__class__.choosen_item_title
        assert self.cart_page.get_added_item_quantity() == '1'

        self.cart_page.click_checkout()

        assert self.cart_page.get_page_loaded_url() == self.checkout_step_one_page.get_url()

    def test_step_4(self):

        self.checkout_step_one_page.fill_first_name('fernando')
        self.checkout_step_one_page.fill_last_name('rodrigues')
        self.checkout_step_one_page.fill_postal_code('21920444')
        self.checkout_step_one_page.click_continue()

        assert self.checkout_step_one_page.get_page_loaded_url() == self.checkout_step_two_page.get_url()

    def test_step_5(self):

        assert self.checkout_step_two_page.get_added_item_title() == self.__class__.choosen_item_title
        assert self.checkout_step_two_page.get_added_item_quantity() == '1'

        self.checkout_step_two_page.click_finish()

        assert self.checkout_step_two_page.get_page_loaded_url() == self.checkout_complete_page.get_url()

    @classmethod
    def tearDownClass(cls):
        cls.login_page.quit_driver()

