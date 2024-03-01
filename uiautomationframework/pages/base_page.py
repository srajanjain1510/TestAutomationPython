from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title: str) -> str:
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def check_web_element_enabled(self, by_locator):
        return self.driver.find_element(by_locator).isEnabled()
