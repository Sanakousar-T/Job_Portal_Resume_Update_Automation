class FounditLoginPage:

    def __init__(self, driver):
         self.driver = driver

    def login_via_password_link(self):
         self.driver.find_element("xpath", "//div[@class='loginWith']").click()

    def email_phone_text_field(self, un):
        self.driver.find_element("xpath", "//input[@id='signInName']").send_keys(un)

    def password_text_field(self, pwd):
        self.driver.find_element("xpath", "//input[@id='password']").send_keys(pwd)

    def login_button(self):
        self.driver.find_element("xpath", "//input[@id='signInbtn']").click()