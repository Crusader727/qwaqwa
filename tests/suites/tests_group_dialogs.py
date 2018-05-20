# -*- coding: utf-8 -*-
import os

import unittest

from tests.pages.auth import AuthPage
from tests.pages.main import MainPage
from tests.pages.message import MessagePage
from tests.pages.dialog import DialogPage
from tests.pages.dialog_menu import DialogMenuPage
from tests.pages.confirm import ConfirmPage

from selenium.webdriver import DesiredCapabilities, Remote

from time import sleep


class TestsGroupDialogs(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.maximize_window()

        self.MESSAGE_TEXT = "testNumber1"
        self.BOT_1_LOGIN = "technopark3"
        self.PASSWORD = os.environ['PASSWORD']
        self.CURRENT_DIALOG_URL = ""
        self.URL_OF_MESSAGES = "https://ok.ru/messages"
        self.ANOTHER_MESSAGE_TEXT = 'new pinned'

        self.dialog_page = DialogPage(self.driver)
        self.message_page = MessagePage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.sign_in(self.BOT_1_LOGIN, self.PASSWORD)
        self.main_page = MainPage(self.driver)
        self.main_page.open_messages()
        self.create_dialog()
        self.dialog_page.add_user_to_chat()        

    def create_dialog(self):
        self.message_page.create_dialog()
        self.message_page.choose_companion()
        self.dialog_page.wait_for_loader()

    def tearDown(self):
        self.driver.get(self.CURRENT_DIALOG_URL)
        self.leave_group_chat()
        self.driver.quit()

    def leave_group_chat(self):
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.leave_chat()
        confirm_page = ConfirmPage(self.driver)
        confirm_page.confirm()

    def test_add_user_to_group_chat(self):
        self.CURRENT_DIALOG_URL = self.driver.current_url                
        self.assertTrue(
            self.dialog_page.get_exsistance_of_created_group_dialog(),
            "test_add_user_to_group_chat failed")

    def test_delete_user_from_group_chat(self):
        self.dialog_page.delete_user_from_chat()
        self.CURRENT_DIALOG_URL = self.driver.current_url        
        self.assertTrue(
            self.dialog_page.get_exsistance_of_delte_companion(),
            "test_delete_user_from_group_chat failed")

    def test_hide_group_chat(self):
        self.dialog_page.wait_for_loader()
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.hide_chat()

        hide_chat_confirm_page = ConfirmPage(self.driver)
        hide_chat_confirm_page.confirm()
        self.CURRENT_DIALOG_URL = self.driver.current_url        
        self.driver.get(self.URL_OF_MESSAGES)
        self.assertTrue(
            self.message_page.get_existance_of_dialogs_empty(),
            "test_hide_group_chat failed")

    def test_pin_message(self):
        self.dialog_page.wait_for_loader()
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.CURRENT_DIALOG_URL = self.driver.current_url        
        self.dialog_page.pin_message()
        self.assertTrue(
            self.dialog_page.exsistance_of_pinned_message(),
            "test_pin_message failed")

    def test_change_pinned_message(self):
        self.dialog_page.wait_for_loader()
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.CURRENT_DIALOG_URL = self.driver.current_url        
        self.dialog_page.pin_message()
        self.dialog_page.send_message(self.ANOTHER_MESSAGE_TEXT)
        self.dialog_page.delete_message()
        self.CURRENT_DIALOG_URL = self.driver.current_url        
        self.dialog_page.pin_message()      
        self.assertTrue(
            self.dialog_page.exsistance_of_pinned_message(),
            "test_change_pinned_message failed")

    def test_unpin_message(self):
        self.dialog_page.wait_for_loader()
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.CURRENT_DIALOG_URL = self.driver.current_url        
        self.dialog_page.pin_message()
        self.dialog_page.unpin_message()
        self.driver.refresh()
        self.assertFalse(
            self.dialog_page.exsistance_of_pinned_message(),
            "test_unpin_message failed")
