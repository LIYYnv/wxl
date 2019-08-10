from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    me_btton = By.ID, "com.yunmall.lc:id/tab_me"

    def click_me(self):
        self.click(self.me_btton)