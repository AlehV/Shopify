import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.add_to_import_page import MainPage
from pages.login_page import LoginPage
from pages.view_import_product_page import ImportPage



def test_buy_product_1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    print("Start test 1")

    login = LoginPage(browser)
    login.authorization()

    allproductsbutton = MainPage(browser)
    allproductsbutton.click_all_products_button()

    mp = MainPage(browser)
    mp.select_products_1()
    mp.select_products_2()
    mp.select_products_3()

    brg = MainPage(browser)
    brg.click_burgers()

    atip = MainPage(browser)
    atip.press_add_to_import_button()

    checknotification = MainPage(browser)
    checknotification.check_notification()

    ip = ImportPage(browser)
    ip.go_to_import_products_page()

    vi = ImportPage(browser)
    vi.view_import_product()

    time.sleep(3)

    op = ImportPage(browser)
    op.open_product_page()

    time.sleep(3)
#Browser switches to a new opened tab!
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    aipp = ImportPage(browser)
    aipp.finish1()

