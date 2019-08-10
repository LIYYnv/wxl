from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_edit_text = By.ID, "com.yunmall.lc:id/logon_account_textview"
    password_edit_text = By.ID, "com.yunmall.lc:id/logon_password_textview"
    login_btn = By.ID, "com.yunmall.lc:id/logon_button"

    def input_username(self, text):
        self.input(self.username_edit_text, text)

    def input_password(self, text):
        self.input(self.password_edit_text, text)

    def click_logon(self):
        self.click(self.login_btn)