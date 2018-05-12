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

        self.dialog_page = DialogPage(self.driver)
        self.message_page = MessagePage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.sign_in("technopark3","testQA1")
        self.main_page = MainPage(self.driver)
        self.main_page.open_messages()

    def tearDown(self):
        self.driver.get(self.CURRENT_DIALOG_URL)
        if(self.dialog_page.no_messages_text_exists() == False):
            self.delete_dialog()
        self.driver.quit()
        
    # def test_create_and_delete_dialog(self):
    #     self.create_dialog()
    #     self.assertEquals(self.dialog_page.send_message_button_exists(), True)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.delete_dialog()
    #     self.driver.get(self.CURRENT_DIALOG_URL)
    #     self.assertEquals(self.dialog_page.no_messages_text_exists(), True)

    # def test_send_sticker(self):
    #     self.create_dialog()
    #     self.dialog_page.send_sticker()
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.assertEquals(self.dialog_page.message_with_sticker_exists(), True)
    
    # def test_send_music(self):
    #     self.create_dialog()
    #     self.dialog_page.send_music()
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.assertEquals(self.dialog_page.sent_message_exists(), True)

    # def test_send_document(self):
    #     self.create_dialog()
    #     self.dialog_page.send_document()
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.assertEquals(self.dialog_page.sent_message_exists(), True)

    # def test_send_photo(self):
    #     self.create_dialog()
    #     self.dialog_page.send_photo()
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.assertEquals(self.dialog_page.sent_message_exists(), True)

    # def test_send_video(self):
    #     self.create_dialog()
    #     self.dialog_page.send_video()
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.assertEquals(self.dialog_page.sent_message_exists(), True)

    # def test_find_dialog(self):
    #     self.create_dialog()
    #     self.dialog_page.find_dialog()
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.assertTrue(self.message_page.get_existance_of_search_result(), "test_find_dialog failed")

    def test_send_message_to_blocked_user(self):
        msg = "awdseq123"
        self.create_dialog()
        self.dialog_page.send_message(msg)
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.driver.delete_all_cookies()
        self.auth_page.sign_in("technopark2","testQA1")
        self.assertEquals(self.main_page.get_new_message_text(), msg)
        self.driver.delete_all_cookies()
        self.auth_page.sign_in("technopark3","testQA1")

    #     self.assertTrue(self.message_page.get_existance_of_search_result(), "test_find_dialog failed")

    def create_dialog(self):
        self.message_page.create_dialog()
        self.message_page.choose_companion()
        self.dialog_page.wait_for_loader()
        
    def delete_dialog(self):
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.delete_dialog()
        delete_dialog_confirm_page = DeleteDialogConfirmPage(self.driver)
        delete_dialog_confirm_page.delete_dialog()
