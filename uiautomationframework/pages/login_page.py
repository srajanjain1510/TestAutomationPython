from uiautomationframework.pages.base_page import BasePage
from uiautomationframework.resources.locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_credentials_and_login(self, username: str, password: str) -> None:
        self.enter_text(LoginPageLocators.lp_user_name_field, username)
        self.enter_text(LoginPageLocators.lp_password_field, password)
        self.click(LoginPageLocators.lp_login_button)

    def navigate_to_url(self, url):
        self.driver.get(url)

    def check_login_button_enabled(self):
        self.check_web_element_enabled(LoginPageLocators.lp_login_button)
