from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FounditUserPage:

    def __init__(self, driver):
        self.driver = driver

    def profile_dropdown(self):
            #self.driver.refresh()
            wait = WebDriverWait(self.driver,10)
            element = wait.until(EC.element_to_be_clickable(("xpath", "//img[@class='rounded-full']")))
            element.click()



    def view_profile(self):
        self.driver.find_element("xpath", "//div[contains(@class,'shadow-user-profile')]//a[.='View Profile']").click()


