class Login:
    textbox_username_id = "ctl00_ContentPlaceHolderBody_txtUserID"
    textbox_password_id = "ctl00_ContentPlaceHolderBody_txtPassword"
    button_login_id = "ctl00_ContentPlaceHolderBody_cmdLogin"
    icon_settings_id = "triggerSettings"
    link_logout_xpath = "//div[@id='divSettingMenu']/div[2]/a[3]"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLoginbtn(self):
        self.driver.find_element_by_id(self.button_login_id).click()
        self.driver.implicitly_wait(50)

    def clicklogout(self):
        self.driver.find_element_by_id(self.icon_settings_id).click()
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()
