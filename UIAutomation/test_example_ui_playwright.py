import re

from playwright.sync_api import Playwright, expect


def test_sample(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title(re.compile("Swag"))
    page.locator(selector="[placeholder=\"Username\"]").fill("standard_user")
    page.locator(selector="[data-test=\"password\"]").fill("secret_sauce")
    page.locator(selector="[data-test=\"login-button\"]").click()

    # ---------------------
    context.close()
    browser.close()

