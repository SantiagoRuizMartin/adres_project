from src.browser import get_driver
from src.pages.authFormPage import AuthPage
from src.pages.mainPagePage import MainPage


def test_try_to_access_auth_form_with_correct_creadentials(driver):
    """Verify that using correct credentials we can access the site."""

    #Define the credentials
    user = "tomsmith"
    password = "SuperSecretPassword!"
     
    #define the pages
    mainPage = MainPage(driver)
    authFormPage = AuthPage(driver)
    
    #Navigate to the page
    driver.get("https://the-internet.herokuapp.com/")
    
    mainPage.click_auth_link()
    
    authFormPage.set_user(user)
    authFormPage.set_password(password)
    authFormPage.click_button()
    
    assert authFormPage.get_logging_message() == 'You logged into a secure area!'.strip()
    assert authFormPage.get_secure_area_message() == "Welcome to the Secure Area. When you are done click logout below."
    
    
def test_try_to_access_auth_form_with_incorrect_creadentials(driver):
    """Verify that using incorrect credentials we can't access the site."""

    #Define the credentials
    user = "incorrectUser"
    password = "IncorrectPassword"

    #Define the pages
    mainPage = MainPage(driver)
    authFormPage = AuthPage(driver)
    
    #Navigate to the page
    driver.get("https://the-internet.herokuapp.com/")

    mainPage.click_auth_link()
    
    authFormPage.set_user(user)
    authFormPage.set_password(password)
    authFormPage.click_button()
    
    assert authFormPage.get_logging_message() == "Your username is invalid!"
