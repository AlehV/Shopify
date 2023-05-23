from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Logout(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser


#Locators
    dashboard = "html/body/div/aside/nav/ul/li[1]/ul/li[1]/a/div"
    account_menu = "html/body/div/div[2]/header/div/div/div[4]/div[1]/button/div"
    sign_out_link = "html/body/div/div[2]/header/div/div/div[4]/div[2]/div/form/button/span"


#Getters
    def get_dashboard(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.dashboard)))

    def get_account_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_menu)))

    def get_sign_out_link(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_out_link)))


       # Actions
    def click_dashboard(self):
        self.get_dashboard().click()
        print("Click dashboard")

    def click_account_menu(self):
        self.get_account_menu().click()
        print("Click account menu")

    def click_sign_out_link(self):
        self.get_sign_out_link().click()
        print("Click sign out button")


    #Methods
    def logout(self):
        self.click_dashboard()
        self.click_account_menu()
        self.click_sign_out_link()
        self.assert_logout_url("https://staging.4partners.lovata.tech/admin/login")



