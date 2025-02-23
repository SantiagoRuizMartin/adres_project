from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class UploadPage(BasePage):
    #Locators
    UPLOAD_FILE_INPUT = (By.ID, 'file-upload')
    UPLOAD_FILE_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILE_NAMES = (By.ID, "uploaded-files")
    DIV_CONTENT = (By.ID, "content")
        
    def add_file_to_upload(self, text):
        """Set text in an input field."""
        self.add_file_to_be_upload(self.UPLOAD_FILE_INPUT, text)  
           
    def click_upload_button(self):
        """Click on a button by its visible text."""
        self.click(self.UPLOAD_FILE_BUTTON)
        
    def get_uploaded_file_name(self):
        """Get the text of the logging message."""
        return self.get_text(self.UPLOADED_FILE_NAMES)    
    
    def get_success_upload_messsage(self):
        """Get the text of the logging message."""
        return self.get_element(self.DIV_CONTENT).find_element(By.TAG_NAME, "h3").text