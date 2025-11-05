import pytest
from pages.foundit_base_page import FounditBasePage
from pages.foundit_login_page import FounditLoginPage
from pages.foundit_profile_page import FounditProfilePage
from pages.foundit_user_page import FounditUserPage
from time import sleep

@pytest.mark.parametrize("launch", ["https://www.foundit.in/"], indirect=True)
def test_foundit_resume_update(launch):
    driver = launch
    foundit_base_page_obj = FounditBasePage(driver)
    foundit_base_page_obj.login_button()
    foundit_loigin_page_obj = FounditLoginPage(driver)
    foundit_loigin_page_obj.login_via_password_link()
    username = "email id"
    foundit_loigin_page_obj.email_phone_text_field(username)
    password = "password"
    foundit_loigin_page_obj.password_text_field(password)
    foundit_loigin_page_obj.login_button()
    foundit_user_page_obj = FounditUserPage(driver)
    foundit_user_page_obj.profile_dropdown()
    foundit_user_page_obj.view_profile()
    file_location = "D:\\sana\\sana\\Resume\\Sanakousar_Tallihal.pdf"
    foundit_profile_page_obj = FounditProfilePage(driver)
    foundit_profile_page_obj.replace_rasume_button(file_location)
    sleep(3)
    print("profile updated, Resume replaced successfully")

