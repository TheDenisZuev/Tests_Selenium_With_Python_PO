from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_match_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        added_book_name = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME).text
        assert book_name == added_book_name, f"Added book is not equal book. Our book {book_name} " \
                                             f"Actual result {added_book_name}"

    def should_be_match_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        cart_total_price = self.browser.find_element(*ProductPageLocators.CART_TOTAL_PRICE).text
        assert book_price == cart_total_price, f"Added book price is not equal count in cart. Our price {book_price} " \
                                               f"Actual result {cart_total_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Element is not disappeared, but should not be"
