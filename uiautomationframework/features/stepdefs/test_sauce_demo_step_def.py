from pytest_bdd import given, when, then, scenarios, parsers

from uiautomationframework.pages.login_page import LoginPage


scenarios('../saucedemo.feature')


@given("Application URL")
def login(initiate_browser_instance):
    LoginPage(initiate_browser_instance).navigate_to_url('https://www.saucedemo.com/')
    # assert LoginPage(initiate_browser_instance).check_login_button_enabled() == True


@when(parsers.parse("login with valid {user} and {password}"))
def enter_credential(initiate_browser_instance,user,password) -> None:
    LoginPage(initiate_browser_instance).enter_credentials_and_login(user, password)


@then("sauce demo home page should be displayed")
def verify_home_page(initiate_browser_instance):
    get_title = LoginPage(initiate_browser_instance).get_title('Swag Labs')
    assert get_title == 'Swag Labs'

# @scenario('../saucedemo.feature',scenario_name="Login to Application")
# def test_sauce_demo():
#     pass
