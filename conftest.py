import pytest
from selenium import webdriver
from splinter import Browser
from pypom import splinter_driver
# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default="chrome",
#                      help="Choose browser: chrome or firefox")
#     parser.addoption('--language', action='store', default='en',
#                      help='Choose language')
#
# @pytest.fixture(scope="class")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     get_url=browser.current_url
#     print(get_url)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = Browser('chrome')
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.fixture
# def browser_name(request):
#     return request.config.getoption("--browser_name")