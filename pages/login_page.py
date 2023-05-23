from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class LoginPage(Base):
    url = "https://staging.4partners.lovata.tech/admin/login"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators
    user_email = "email"
    password = "#password"
    login_button = "html/body/div/div[1]/form[1]/button"
    main_word = "html/body/div/div[2]/div[1]/div/div/header/div/h1"

    # Getters
    def get_user_email(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, self.user_email)))

    def get_password(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def input_user_email(self, user_email):
        self.get_user_email().send_keys(user_email)
        print("Input user email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods
    def authorization(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.get_current_url()
        self.input_user_email("admin@5partners.io")
        self.input_password("password1")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Dashboard")



