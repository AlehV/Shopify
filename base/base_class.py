class Base():
    def __init__(self, browser):
        self.browser = browser

    """Method Get current url"""
    def get_current_url(self):
        get_url = self.browser.current_url
        print("Current url " + get_url)

    """Method user is on dashboard"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("User is on Dashboard Page")

    """Assert url"""
    def assert_all_products_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print("User is on log in page")

    """Add to import notification"""
    def added_to_import_notification(self, word, result):
        added_to_import_notification_text = word.text
        assert added_to_import_notification_text == result
        print("Products added to import")

    """Assert import product url"""
    def assert_import_product_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print("Import product page opened")

    """Assert logout url"""
    def assert_logout_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print(result)
        print("User logged out")