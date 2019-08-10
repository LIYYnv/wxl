from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):
    login_username = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    def get_username(self):
        return self.find_element(self.login_username).text