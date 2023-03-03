"""商品列表页"""
import time

"""商品列表页"""
from __init__ import color_of_body, memory_capacity
from base.base import BasePage, BaseHndle, base_switching_window


class PageDetaillsPage(BasePage):
    def __init__(self):
        super().__init__()
        self.color_of_body = color_of_body  # 机身颜色
        self.memory_capacity = memory_capacity  # 存储容量

    def page_color_of_body(self,text):
        body = (self.color_of_body[0], self.color_of_body[1].format(text))
        return self.base_find(body)

    def page_memory_capacity(self,texts):
        capacity = (self.memory_capacity[0], self.memory_capacity[1].format(texts))
        return self.base_find(capacity)


class HandleDetaillsPage(BaseHndle):
    def __init__(self):
        self.page_product = PageDetaillsPage()

    def handle_color_of_body(self,body):
        base_switching_window()
        time.sleep(10)
        self.base_click(self.page_product.page_color_of_body(body))

    def handle_memory_capacity(self,capacity):
        self.base_click(self.page_product.page_memory_capacity(capacity))


class ProxyDetaillsPage(object):
    def __init__(self):
        self.handle_detaills_page = HandleDetaillsPage()

    def proxy_add_shopping_cart(self,body,capacity):
        self.handle_detaills_page.handle_color_of_body(body)
        self.handle_detaills_page.handle_memory_capacity(capacity)
