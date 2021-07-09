from selenium import webdriver
import pytest
import platform

base_url = "http://jt-dev.azurewebsites.net/#/SignUp"


@pytest.fixture()
def setup():
    os = platform.system()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if os == "Windows":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver_win32.exe", options=options)
    elif os == "Linux":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver_linux64", options=options)
    else:
        driver = webdriver.Chrome(executable_path="drivers/chromedriver_mac64", options=options)

    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()
