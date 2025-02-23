from pathlib import Path
from src.pages.mainPagePage import MainPage
from src.pages.upload_file_page import UploadPage


def test_try_to_access_auth_form_with_correct_creadentials(driver):
    """Verify that we are able to upload a file."""

    #define the pages
    mainPage = MainPage(driver)
    uploadFilePage = UploadPage(driver)
    
    #Navigate to the page
    driver.get("https://the-internet.herokuapp.com/")
    
    mainPage.click_upload_file()
    
    #file_path helps to locate the file to be uploaded
    file_path = Path(__file__).resolve().parent.parent / "data" / "country_full.csv"
    #Add the file to be uploaded
    uploadFilePage.add_file_to_upload(str(file_path))
    uploadFilePage.click_upload_button()
    
    #Confirm that the file was uploaded
    assert uploadFilePage.get_uploaded_file_name() == "country_full.csv"
    assert uploadFilePage.get_success_upload_messsage() == "File Uploaded!"