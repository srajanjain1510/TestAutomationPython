from selenium import webdriver




def test_ui_with_docker_image():

    options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-ssl-errors=yes')
    # options.add_argument('--ignore-certificate-errors')
    options.set_capability("platformName",'linux')
    options.set_capability("browserVersion", "122")
    hub_url = "http://localhost:4444/wd/hub"
    driver = webdriver.Remote(command_executor=hub_url, options=options)
    print(driver.session_id)

    driver.get("http://www.browserstack.com/")
