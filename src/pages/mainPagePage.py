from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage

class MainPage(BasePage):
    #Locators
    FORM_AUTHENTICATION = (By.LINK_TEXT, 'Form Authentication')
    UPLOAD_FILE = (By.LINK_TEXT, 'File Upload')
        
    def click_auth_link(self):
        """Click on a link by its visible text."""
        self.click(self.FORM_AUTHENTICATION)
        
    def click_upload_file(self):
        """Click on a link by its visible text."""
        self.click(self.UPLOAD_FILE)