from base_element import BaseElement

class AttachForm(BaseElement):
    MUSIC_BUTTON = '//a[@data-l="t,musicLink"]'

    def get_music_button(self):
        return self.get_button_by_xpath(self.MUSIC_BUTTON)
