from selenium.webdriver.support.ui import WebDriverWait

class BaseElement(object):
    locator = None
    element = None
    DEFAULT_WAIT_TIME = 30

    def __init__(self, driver):
        self.driver = driver
    
    def wait_until_find_by_xpath(self,xpath):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(xpath)
            )
    def wait_for_presence(self):
         return WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.presence_of_element_located(self.locator)
        )

    def wait_for_clickable(self):
        return WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.element_to_be_clickable(self.locator)
        )
         
    def wait_for_visible(self):
        return WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.visibility_of_element_located(self.locator)
        )

    def wait_for_alert(self):
        return WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.alert_is_present()
        )

    def __getattr__(self, item):
        def f():
            self.locator = self.__getattribute__(item.upper())
            return self
        return f