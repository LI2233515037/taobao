import time
import unittest

from page.page_home import ProxyHome
from page.product_details_page import ProxyDetaillsPage

from page.product_list import ProxyProduct
from utlis import BrowserObject
from __init__ import taobao


class TestTaoBaoProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserObject.get_driver()
        cls.home_search = ProxyHome()
        cls.product_list = ProxyProduct()
        cls.detaills_page = ProxyDetaillsPage()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        BrowserObject.quit_driver()

    def setUp(self) -> None:
        self.driver.get(taobao)

    def test_tao_bao_product(self):
        self.home_search.proxy_search("小米手机")
        self.product_list.proxy_commodity()
        time.sleep(10)
        self.detaills_page.proxy_add_shopping_cart("神秘黑境", "6+128GB")


if __name__ == '__main__':
    unittest.main()
