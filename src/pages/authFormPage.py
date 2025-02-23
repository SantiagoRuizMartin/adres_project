from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class AuthPage(BasePage):
    #Locators
    FORM_AUTHENTICATION = (By.LINK_TEXT, 'Form Authentication')
    USER = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGGIN_BUTTON = (By.CLASS_NAME, "radius")
    LOGGIN_MESSAGE = (By.CLASS_NAME,  "flash")
    SECURE_AREA_MESSAGE =(By.CLASS_NAME, 'subheader')
        
    def set_user(self, text):
        """Set text in an input field."""
        self.enter_text(self.USER, text)  
          
    def set_password(self, text):
        """Set password in an input field."""
        self.enter_text(self.PASSWORD, text)      
        
    def click_button(self):
        """Click on a button by its visible text."""
        self.click(self.LOGGIN_BUTTON)
    
    def get_logging_message(self):
        """Check if the success message is displayed."""
        actual_text = self.get_text(self.LOGGIN_MESSAGE).strip()
        return actual_text.replace("\n", "").replace("×", "").strip()
    
    def get_secure_area_message(self):
        """Check if the secure area message is displayed."""
        return self.get_text(self.SECURE_AREA_MESSAGE).strip()