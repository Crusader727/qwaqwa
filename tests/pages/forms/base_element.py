from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class BaseElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_button_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
            
    def get_field_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))
    
    def existance_of_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException as e:
            return False
        return True
        
    # def get_elements_by_xpath(self, xpath):
    #     return self.driver.find_elements_by_xpath(xpath)
        
