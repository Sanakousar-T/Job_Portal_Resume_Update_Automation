class NaukriProfilePage:

    def __init__(self, driver):
        self.driver = driver

    def update_resume(self, resume):
        self.driver.find_element("xpath", "//div[@class='uploadContainer']//input[@id='attachCV']").send_keys(resume)


