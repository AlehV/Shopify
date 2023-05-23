from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class MainPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

#Locators
    all_products_button = "html/body/div/aside/nav/ul/li[3]/ul/li[3]/a/div/span"
    select_product_1 = "html/body/div/div[2]/div[1]/div/div/div/div/div[3]/table/tbody/tr[1]/td[2]/label/input"
    select_product_2 = "html/body/div/div[2]/div[1]/div/div/div/div/div[3]/table/tbody/tr[2]/td[2]/label/input"
    select_product_3 = "html/body/div/div[2]/div[1]/div/div/div/div/div[3]/table/tbody/tr[3]/td[2]/label/input"
    burger = "body > div > div.filament-main.flex-col.gap-y-6.w-screen.flex-1.rtl\:lg\:pl-0.flex.lg\:pl-\[var\(--sidebar-width\)\].rtl\:lg\:pr-\[var\(--sidebar-width\)\] > div.filament-main-content.flex-1.w-full.px-4.mx-auto.md\:px-6.lg\:px-8.max-w-7xl > div > div > div > div > div.filament-tables-header-container > div > div:nth-child(1) > div > div.filament-dropdown-trigger.cursor-pointer > button > svg"
    add_to_import_button = "html/body/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/button/span"
    notification = "html/body/div/div[2]/header/div/div/div[3]/div[1]/div/div/div/p"

#Getters
    def get_all_products_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.all_products_button)))

    def get_select_product_1(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_burger(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.burger)))

    def get_add_to_import_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_import_button)))

    def get_notification(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.notification)))

       # Actions
    def click_all_products_button(self):
        self.get_all_products_button().click()
        print("Click all products button")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click Select product 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click Select product 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click Select product 3")

    def click_burger(self):
        self.get_burger().click()
        print("Click burger button")

    def click_add_to_import_button(self):
        self.get_add_to_import_button().click()
        print("Click add_to_import_button")

    def check_notification(self):
        self.get_notification().click()
        print("Click link about")
        self.added_to_import_notification(self.get_notification(), "Products added to import")

    #Methods
    def all_product_button(self):
        self.get_current_url()
        self.get_all_products_button()
        self.click_all_products_button()

    def select_products_1(self):
        self.click_select_product_1()

    def select_products_2(self):
        self.click_select_product_2()

    def select_products_3(self):
        self.click_select_product_3()

    def click_burgers(self):
        self.click_burger()

    def press_add_to_import_button(self):
        self.click_add_to_import_button()

    def add_to_import_notification(self):
        self.get_current_url()
        self.check_notification()



