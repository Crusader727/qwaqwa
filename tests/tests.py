# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from pages.auth import AuthPage
from pages.main import MainPage
from pages.message import MessagePage
from pages.dialog import DialogPage
from pages.dialog_menu import DialogMenuPage
from pages.confirm import ConfirmPage
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
        self.URL_OF_DIALOG_WITH_ME = "https://ok.ru/messages/575662066926"

    def tearDown(self):
        self.driver.get(self.CURRENT_DIALOG_URL)
        if(self.CURRENT_DIALOG_URL[23] == 'c'):
            self.leave_group_chat()
        else:
            if(self.dialog_page.no_messages_text_exists() == False):
                self.delete_dialog()
        self.driver.quit()
    
    def leave_group_chat(self):                      
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.leave_chat()
        confirm_page = ConfirmPage(self.driver)
        confirm_page.confirm()
    
    def create_dialog(self):
        self.message_page.create_dialog()
        self.message_page.choose_companion()
        self.dialog_page.wait_for_loader()
        
    def delete_dialog(self):
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.delete_dialog()
        confirm_page = ConfirmPage(self.driver)
        confirm_page.confirm()

        
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

    # def test_send_message_to_blocked_user(self):
    #     MESSAGE_TEXT = 'TestNumber1'
    #     self.create_dialog()
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.driver.delete_all_cookies()
    #     self.auth_page.sign_in("technopark2","testQA1")
    #     self.assertEquals(self.main_page.get_new_message_text(), MESSAGE_TEXT)
    #     self.driver.delete_all_cookies()
    #     self.auth_page.sign_in("technopark3","testQA1")

    # def test_send_message_to_unblocked_user(self):
    #     MESSAGE_TEXT = 'TestNumber1'
    #     self.create_dialog()
    #     self.dialog_page.unblock_user()
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.dialog_page.block_user()
    #     self.driver.delete_all_cookies()
    #     self.auth_page.sign_in("technopark2","testQA1")
    #     self.assertEquals(self.main_page.get_new_message_text(), MESSAGE_TEXT)
    #     self.driver.delete_all_cookies()
    #     self.auth_page.sign_in("technopark3","testQA1")
   
    # def test_get_message_from_blocked_user(self):
    #     MESSAGE_TEXT = 'TestNumber1'
    #     self.driver.delete_all_cookies()
    #     self.auth_page.sign_in("technopark2","testQA1")
    #     self.driver.get(self.URL_OF_DIALOG_WITH_ME)
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.driver.delete_all_cookies()
    #     self.auth_page.sign_in("technopark3","testQA1")
    #     self.assertTrue(not self.main_page.get_existance_of_new_message(), "test_get_message_from_blocked_user failed")
    #     self.driver.delete_all_cookies()
    #     self.auth_page.sign_in("technopark2","testQA1")

    #112Nick

    # def test_send_message(self):      
    #     MESSAGE_TEXT = 'TestNumber1'  
    #     self.create_dialog()
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.assertTrue(self.dialog_page.sent_message_exists(), "test send message failed")

    # def test_edit_message(self):              
    #     MESSAGE_TEXT = 'TestNumber1'  
    #     MESSAGE_EDITED_TEXT = ' IS_EDITED'      
    #     self.create_dialog()
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.dialog_page.edit_and_send_message(MESSAGE_EDITED_TEXT) 
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.driver.refresh()
    #     self.assertEquals(self.dialog_page.get_sent_message_text(), MESSAGE_TEXT + MESSAGE_EDITED_TEXT)

    # def test_delete_message(self):         
    #     MESSAGE_TEXT = 'TestNumber1'          
    #     self.create_dialog()
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.dialog_page.delete_message()#
    #     self.driver.refresh()
    #     self.assertTrue(self.dialog_page.no_messages_text_exists(), "test_delete_message failed")

    # def test_answer_message(self):
    #     MESSAGE_TEXT = 'TestNumber1'  
    #     MESSAGE_ANSWERED_TEXT = ' IS_ANSWERED'  
    #     self.create_dialog()
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.dialog_page.answer_message(MESSAGE_ANSWERED_TEXT)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.driver.refresh()
    #     self.assertTrue(self.dialog_page.get_exsistance_of_answered_message(), "test_answer_message failed")

    # def test_forward_message(self):
    #     MESSAGE_TEXT = 'TestNumber1'      
    #     self.create_dialog()
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.dialog_page.forward_message()
    #     self.message_page.choose_companion_forward_message()
    #     self.assertTrue(self.dialog_page.get_exsistance_of_forwarded_message(), "test_forward_message failed")

    # def test_find_message(self):           
    #     self.create_dialog()  
    #     MESSAGE_TEXT = 'TestNumber1'  
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url
    #     self.dialog_page.find_message(MESSAGE_TEXT)
    #     self.assertEquals(MESSAGE_TEXT, self.message_page.get_found_message_text())

    # def test_add_user_to_group_chat(self):
    #     self.create_dialog()
    #     self.dialog_page.add_user_to_chat()
    #     self.assertTrue(self.dialog_page.get_exsistance_of_created_group_dialog(), "test_add_user_to_group_chat failed")
    #     self.CURRENT_DIALOG_URL = self.driver.current_url

    # def test_delete_user_from_group_chat(self):
    #     self.create_dialog()
    #     self.dialog_page.add_user_to_chat()
    #     self.dialog_page.delete_user_from_chat() 
    #     self.assertTrue(self.dialog_page.get_exsistance_of_delte_companion(), "test_delete_user_from_group_chat failed")
    #     self.CURRENT_DIALOG_URL = self.driver.current_url

    # def test_hide_group_chat(self):
    #     self.create_dialog()
    #     self.dialog_page.add_user_to_chat()
    #     self.dialog_page.wait_for_loader()
    #     self.dialog_page.open_menu()
    #     dilog_menu_page = DialogMenuPage(self.driver)
    #     dilog_menu_page.hide_chat()
    #     self.CURRENT_DIALOG_URL = self.driver.current_url        
    #     hide_chat_confirm_page = ConfirmPage(self.driver)
    #     hide_chat_confirm_page.confirm()
    #     self.driver.get("https://ok.ru/messages")
    #     self.assertTrue(self.message_page.get_existance_of_dialogs_empty(), "test_hide_group_chat failed") 

    # def test_pin_message(self):
    #     MESSAGE_TEXT = 'TestNumber1'  
    #     self.create_dialog()
    #     self.dialog_page.add_user_to_chat()
    #     self.dialog_page.wait_for_loader()
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url        
    #     self.dialog_page.pin_message()
    #     self.assertTrue(self.dialog_page.exsistance_of_pinned_message(), "test_pin_message failed") 
        
    # def test_unpin_message(self):
    #     MESSAGE_TEXT = 'TestNumber1'  
    #     self.create_dialog()
    #     self.dialog_page.add_user_to_chat()
    #     self.dialog_page.wait_for_loader()
    #     self.dialog_page.send_message(MESSAGE_TEXT)
    #     self.CURRENT_DIALOG_URL = self.driver.current_url        
    #     self.dialog_page.pin_message()
    #     self.dialog_page.unpin_message()
    #     self.driver.refresh()
    #     self.assertTrue(not self.dialog_page.exsistance_of_pinned_message(), "test_unpin_message failed") 