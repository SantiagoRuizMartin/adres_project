from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        #Added a global wait time of 10 seconds
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text
    
    def add_file_to_be_upload(self, by_locator, text):
        file_input = self.wait.until(EC.visibility_of_element_located(by_locator))
        file_input.send_keys(text)
        
    def get_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))
