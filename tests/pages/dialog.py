import os
from base_page import BasePage
from forms.dialog_form import DialogForm
from forms.attach_form import AttachForm

class DialogPage(BasePage):
    
    def __init__(self, driver):
        super(DialogPage, self).__init__(driver)
        self.dialog_form = DialogForm(self.driver)
        self.attach_form = AttachForm(self.driver)

    def open_menu(self): 
        self.dialog_form.get_menu_button().click()

    def send_message_button_exists(self):
        return self.dialog_form.get_send_message_button_exists()

    def no_messages_text_exists(self):
        return self.dialog_form.get_no_messages_text_exists() 
    
    def send_sticker(self):
        self.dialog_form.get_sticker_button().click()
        self.dialog_form.get_sticker_list_button().click()
        self.dialog_form.get_unsmile_sticker().click()
    
    def message_with_sticker_exists(self):
        return self.dialog_form.get_message_with_sticker()

    def sent_message_exists(self):
        return self.dialog_form.get_sent_message()

    def send_music(self):
        self.dialog_form.get_attach_button().click()
        self.attach_form.get_music_button().click()
        self.attach_form.get_song().click()
        self.attach_form.get_send_song_button().click()

    def send_document(self):
        self.dialog_form.get_attach_button().click()
        self.attach_form.get_document_input().send_keys(os.getcwd()+"/tests/static/awd.txt")

    def send_photo(self):
        self.dialog_form.get_attach_button().click()
        self.attach_form.get_photo_input().send_keys(os.getcwd()+"/tests/static/sabaton.jpg")
        if(self.attach_form.get_loader()):
            self.dialog_form.get_send_message_button().click()
        
    def send_video(self):
        self.dialog_form.get_attach_button().click()
        self.attach_form.get_video_button().click()
        self.attach_form.get_video_input().send_keys(os.getcwd()+"/tests/static/sabaton.mp4")
        if(self.attach_form.get_loader()):
            self.dialog_form.get_send_message_button().click()
       