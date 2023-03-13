from selenium.webdriver.support.wait import WebDriverWait

from utlis import BrowserObject
from __init__ import scroll_bar, tianmao_cookies


class BasePage:
    def __init__(self, ):
        self.drvier = BrowserObject.get_driver()

    def base_find(self, loc, timeout=30, poll=0.5):  # 获取元素
        return WebDriverWait(self.drvier, timeout=timeout, poll_frequency=poll).until(lambda a: a.find_element(*loc))


class BaseHandle():

    def base_import(self, element, value):  # 输入文本
        text = element
        text.clear()
        text.send_keys(value)

    def base_click(self, element):  # 点击元素
        element.click()

    def base_text(self):  # 获取文本
        pass


class base_operation():
    def __init__(self):
        self.driver = BrowserObject.get_driver()

    def base_scroll_bar(self, scroll, bar):  # 滚动条
        js = scroll_bar.format(scroll, bar)
        self.driver.execute_script(js)

    def base_switching_window(self):  # 切换窗口
        # print("当前页面句柄", self.driver.current_window_handle)
        a = self.driver.window_handles
        # print(a)
        self.driver.switch_to.window(a[-1])
        # print("切换后页面句柄", self.driver.current_window_handle)

    def base_refresh(self):  # 刷新页面
        self.driver.refresh()

    def base_tabao_cookies(self):  # 淘宝cookies
        self.driver.delete_all_cookies()
        for cookie in tianmao_cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
