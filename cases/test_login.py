import time

from base.base_driver import get_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        self.page.home.click_me()
        self.page.register.click_login()
        self.page.login.input_username("itheima_test")
        self.page.login.input_password("itheima")
        self.page.login.click_logon()
        time.sleep(2)
        assert self.page.me.get_username() == "itheima_test", "用户名与登录时的用户名不一致"
