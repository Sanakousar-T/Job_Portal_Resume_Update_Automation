class LoginForm:
    def __init__(self, driver):
        self.driver = driver

    def email_username_text_field(self, un):
        self.driver.find_element("xpath", "//form[@name='login-form']//input[contains(@placeholder,'Enter your active Email')]").send_keys(un)

    def password_text_field(self, pwd):
        self.driver.find_element("xpath","//form[@name='login-form']//input[contains(@placeholder,'password')]").send_keys(pwd)

    def login_button(self):
        self.driver.find_element("xpath","//button[.='Login']").click()
