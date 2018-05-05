# -*- coding: utf-8 -*-

import os
from time import sleep
import unittest
import urlparse

from pages.auth import AuthPage, MainPage

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Main(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.sign_in("technopark3","testQA1")
        main_page = MainPage(self.driver)
        main_page.open_messages()
        sleep(20000)
