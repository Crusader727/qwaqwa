# -*- coding: utf-8 -*-

import os
from time import sleep
import unittest
import urlparse

from pages.auth import AuthPage
from pages.main import MainPage
from pages.message import MessagePage
from pages.dialog import DialogPage
from pages.dialog_menu import DialogMenuPage
from pages.delete_dialog_confirm import DeleteDialogConfirmPage


from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Tests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    #def test(self):
        

    def test_create_and_delete_dialog(self):
        auth_page = AuthPage(self.driver)
        auth_page.sign_in("technopark3","testQA1")
        main_page = MainPage(self.driver)
        main_page.open_messages()
        sleep(1)
        message_page = MessagePage(self.driver)
        message_page.create_dialog()
        message_page.choose_companion()
        sleep(2)
        dialog_page = DialogPage(self.driver)
        dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.delete_dialog()
        delete_dialog_confirm_page = DeleteDialogConfirmPage(self.driver)
        delete_dialog_confirm_page.delete_dialog()
        # sleep(10)