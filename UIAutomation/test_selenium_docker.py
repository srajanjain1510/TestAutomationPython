import re

from selenium import webdriver


def test_ui_with_docker_image():
    options = webdriver.ChromeOptions()
    hub_url = "http://localhost:4444"
    driver = webdriver.Remote(command_executor=hub_url, options=options)
    print(driver.session_id)
    driver.get("http://www.browserstack.com/")
