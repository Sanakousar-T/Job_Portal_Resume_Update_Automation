class FounditBasePage:

    def __init__(self, driver):
        self.driver = driver

    def login_button(self):
        self.driver.find_element("xpath", "//div[@id='seekerHeader']//button[.='Login']").click()

