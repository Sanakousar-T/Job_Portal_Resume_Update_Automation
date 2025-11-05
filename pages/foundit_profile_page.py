from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FounditProfilePage:

    def __init__(self, driver):
        self.driver = driver

    def replace_rasume_button(self, resume):
        self.driver.find_element("xpath", "//input[@class='hidden']").send_keys(resume)



