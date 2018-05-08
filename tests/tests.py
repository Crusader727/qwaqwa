# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from pages.auth import AuthPage
from pages.main import MainPage
from pages.message import MessagePage
from pages.dialog import DialogPage
from pages.dialog_menu import DialogMenuPage
from pages.delete_dialog_confirm import DeleteDialogConfirmPage
from time import sleep

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Tests(unittest.TestCase):

    CURRENT_DIALOG_URL = ""

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.sign_in("technopark3","testQA1")
        main_page = MainPage(self.driver)
        main_page.open_messages()

    def tearDown(self):
        self.driver.get(self.CURRENT_DIALOG_URL)
        dialog_page = DialogPage(self.driver)
        if(dialog_page.no_messages_text_exists() == False):
            self.delete_dialog()
        self.driver.quit()
        
    def test_create_and_delete_dialog(self):
        self.create_dialog()
        dialog_page = DialogPage(self.driver)
        self.assertEquals(dialog_page.send_message_button_exists(), True)
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.delete_dialog()
        self.driver.get(self.CURRENT_DIALOG_URL)
        self.assertEquals(dialog_page.no_messages_text_exists(), True)


    def create_dialog(self):
        message_page = MessagePage(self.driver)
        message_page.create_dialog()
        message_page.choose_companion()
        
    def delete_dialog(self):
        dialog_page = DialogPage(self.driver)
        dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.delete_dialog()
        delete_dialog_confirm_page = DeleteDialogConfirmPage(self.driver)
        delete_dialog_confirm_page.delete_dialog()
