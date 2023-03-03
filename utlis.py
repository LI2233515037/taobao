"""浏览器驱动对象"""
import time

from selenium import webdriver
from __init__ import taobao,jing_dong,cookies


class BrowserObject():
    driver = None
    quit_status = True

    @classmethod
    def get_driver(cls):  # 创建浏览器对象
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get(taobao)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
            cls.driver.delete_all_cookies()
            for cookie in cookies:
                cls.driver.add_cookie(cookie)
            cls.driver.refresh()
        return cls.driver

    @classmethod
    def quit_driver(cls):  # 关闭浏览器对象
        if cls.driver:
            cls.driver.quit()
            cls.driver = None

    @classmethod
    def modify_browser_exit(cls, status):  # 修改退出浏览器方法
        cls.quit_status = status


if __name__ == '__main__':
    BrowserObject.get_driver()
    time.sleep(3)
    BrowserObject.quit_driver()