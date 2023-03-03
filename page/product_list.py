"""商品列表页"""
from __init__ import commodity
from base.base import BasePage, BaseHndle


class PageProduct(BasePage):
    def __init__(self):
        super().__init__()
        self.commodity = commodity

    def page_commodity(self,):
        return self.base_find(self.commodity)


class HandleProduct(BaseHndle):
    def __init__(self):
        self.page_product = PageProduct()

    def handle_commodity(self):
        self.base_click(self.page_product.page_commodity())


class ProxyProduct():
    def __init__(self):
        self.handle_product = HandleProduct()

    def proxy_commodity(self):
        self.handle_product.handle_commodity()
