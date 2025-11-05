
class NaukriBasePage:

    def __init__(self, driver):
        self.driver = driver

    def login_link(self):
        self.driver.find_element("xpath", "//a[.='Login']").click()


