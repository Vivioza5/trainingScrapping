from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from selenium.common.exceptions import NoAlertPresentException
import math
from splinter import Browser
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators, MainPageLocators, MainLocators
from pypom import splinter_driver
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        self.browser.find_by_css(MainLocators.LINK).click()