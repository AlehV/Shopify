from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ImportPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

#Locators
    products_to_import_tab_button = "html/body/div/aside/nav/ul/li[5]/ul/li/a/div/span"
    view_button = "html/body/div/div[2]/div[1]/div/div/div/div/div[3]/table/tbody/tr[1]/td[7]/div/a[2]"
    open_product_button = "html/body/div/div[2]/div[1]/div/div/header/div[2]/a[2]/span"


#Getters
    def get_products_to_import_tab_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.products_to_import_tab_button)))

    def get_view_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.view_button)))

    def get_open_product_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_product_button)))


       # Actions
    def click_products_to_import_tab_button(self):
        self.get_products_to_import_tab_button().click()
        print("Click products to import tab")

    def click_view_button(self):
        self.get_view_button().click()
        print("Click view button")

    def click_open_product_button(self):
        self.get_open_product_button().click()
        print("Click open product page button")


    #Methods
    def go_to_import_products_page(self):
        self.get_current_url()
        self.click_products_to_import_tab_button()

    def view_import_product(self):
        self.get_current_url()
        self.click_view_button()

    def open_product_page(self):
        self.click_open_product_button()

    def finish1(self):
        self.get_current_url()
        self.assert_import_product_url("https://baumbach.biz/odit-aut-eligendi-sit-et-maiores-distinctio-a.html")

