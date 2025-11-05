

class NaukriHomePage:

    def __init__(self, driver):
        self.driver = driver

    def view_profile_link(self):
        self.driver.find_element("xpath", "//div[contains(@class,'info-wrapper')]//a[@href='/mnjuser/profile']").click()



