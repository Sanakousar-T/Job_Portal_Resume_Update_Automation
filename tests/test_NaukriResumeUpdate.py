from time import sleep
import pytest
from pages.naukri_base_page import NaukriBasePage
from pages.naukri_homepage import NaukriHomePage
from pages.naukri_login_form import LoginForm
from pages.naukri_profile_page import NaukriProfilePage

#@pytest.mark.skip
@pytest.mark.parametrize("launch", ["https://www.naukri.com/"], indirect=True)
def test_naukri_resume_update(launch):
    driver = launch
    naukri_base_page_obj = NaukriBasePage(driver)
    naukri_base_page_obj.login_link()
    loginform = LoginForm(driver)
    username = "emai id"
    password = "password"
    loginform.email_username_text_field(username)
    loginform.password_text_field(password)
    loginform.login_button()
    naukri_homepage_obj = NaukriHomePage(driver)
    naukri_homepage_obj.view_profile_link()
    naukri_profile_page_obj = NaukriProfilePage(driver)
    file_location = "D:\\sana\\sana\\Resume\\Sanakousar_Tallihal.pdf"
    naukri_profile_page_obj.update_resume(file_location)
    sleep(3)
    print("Naukri profile updated, Resume uploaded successfully")