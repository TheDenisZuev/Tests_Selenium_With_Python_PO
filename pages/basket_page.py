from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket is not empty and have items"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Message about empty basket in not find"



