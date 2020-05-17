from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")

class ProductPageLocators():
    ADD_CART_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']//button[@type='submit']")
    BOOK_NAME = (By.XPATH, "//h1")
    BOOK_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']//p[@class='price_color']")
    CART_TOTAL_PRICE = (By.XPATH, "//div[@class='alertinner ']//p//strong")
    ADDED_BOOK_NAME = (By.XPATH, "(//div[@id='messages']//strong)[1]")
    SUCCESS_MESSAGE = (By.XPATH, "(//div[@id='messages']//div[@class='alertinner '])[1]")

class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")