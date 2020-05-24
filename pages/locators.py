from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")
    REGISTRATION_EMAIL_FIELD = (By.XPATH, "//input[@id='id_registration-email']")
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, "//input[@id='id_registration-password1']")
    REGISTRATION_PASSWORD_FIELD_CONFIRM = (By.XPATH, "//input[@id='id_registration-password2']")
    REGISTRATION_BUTTON_CONFIRM = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    ADD_CART_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']//button[@type='submit']")
    BOOK_NAME = (By.XPATH, "//h1")
    BOOK_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']//p[@class='price_color']")
    CART_TOTAL_PRICE = (By.XPATH, "//div[@class='alertinner ']//p//strong")
    ADDED_BOOK_NAME = (By.XPATH, "(//div[@id='messages']//strong)[1]")
    SUCCESS_MESSAGE = (By.XPATH, "(//div[@id='messages']//div[@class='alertinner '])[1]")

class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    BASKET_LINK = (By.XPATH, "//span[@class='caret']/parent::*/preceding-sibling::a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEM = (By.XPATH, "//div[@class='basket-items']")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")