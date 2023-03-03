"""首页"""

from __init__ import search,search_button
from base.base import BasePage, BaseHndle


class PageHome(BasePage):
    def __init__(self):
        super().__init__()
        self.search = search  # 搜索框
        self.search_button= search_button#点击搜索按钮

    def page_search(self):#
        return self.base_find(self.search)
    def page_search_button(self):
        return self.base_find(self.search_button)


class HandleHome(BaseHndle):
    def __init__(self):
        self.page_home = PageHome()

    def handle_search(self, element):
        self.base_import(self.page_home.page_search(), element)
    def handle_search_button(self):
        self.base_click(self.page_home.page_search_button())


class ProxyHome():
    def __init__(self):
        self.handle_home = HandleHome()

    def proxy_search(self, element):#搜索商品
        self.handle_home.handle_search(element)
        self.handle_home.handle_search_button()
