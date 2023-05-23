from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.logout_page import Logout


def test_logout_process():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)


    login = LoginPage(browser)
    login.authorization()

    loginpage = Logout(browser)
    loginpage.logout()

