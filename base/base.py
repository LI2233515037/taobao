from selenium.webdriver.support.wait import WebDriverWait

from utlis import BrowserObject


class BasePage:
    def __init__(self, ):
        self.drvier = BrowserObject.get_driver()

    def base_find(self, loc, timeout=30, poll=0.5):  # 获取元素
        return WebDriverWait(self.drvier, timeout=timeout, poll_frequency=poll).until(lambda a: a.find_element(*loc))



class BaseHndle():

    def base_import(self, element, value):  # 输入文本
        text = element
        text.clear()
        text.send_keys(value)

    def base_click(self, element):  # 点击元素
        element.click()

    def base_text(self):  # 获取文本
        pass


def base_switching_window():
    driver= BrowserObject.get_driver()
    print("当前页面句柄",driver.current_window_handle)
    a = driver.window_handles
    print(a)
    driver.switch_to.window(a[-1])
    print("切换后页面句柄",driver.current_window_handle)
