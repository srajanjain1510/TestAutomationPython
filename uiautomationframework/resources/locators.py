from selenium.webdriver.common.by import By


class LoginPageLocators:
    lp_user_name_field = (By.ID, 'user-name')
    lp_password_field = (By.ID, 'password')
    lp_login_button = (By.ID, 'login-button')
