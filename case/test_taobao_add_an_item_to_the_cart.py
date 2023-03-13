"""添加商品到购物车"""

import time
import unittest

from page.jd_add_to_shopping_cart import ProxyShopping
from page.jd_page_home import ProxyHome
from page.jd_product_details_page import ProxyDetaillsPage

from page.jd_product_list import ProxyProduct
from utlis import BrowserObject
from __init__ import jing_dong,picture_path,timestamp


class TestTaoBaoProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserObject.get_driver()
        cls.home_search = ProxyHome()
        cls.product_list = ProxyProduct()
        cls.detaills_page = ProxyDetaillsPage()
        cls.proxy_shopping_cart = ProxyShopping()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        BrowserObject.quit_driver()

    def setUp(self) -> None:
        time.sleep(3)
        self.driver.get(jing_dong)

    def test_tao_bao_product(self):
        self.home_search.proxy_search("小礼物")
        self.product_list.proxy_commodity("尚韵 生日礼物女 小羊公仔玩偶520七夕情人节女友毕业礼物送女生毛绒玩具布偶娃娃公仔儿童玩具")
        self.detaills_page.proxy_add_shopping_cart("波克小羊【灯光+礼盒】")

        try:
            time.sleep(5)
            text = self.proxy_shopping_cart.proxy_successfully_added_to_cart()
            self.assertIn("商品已成功加入购物车", text)
        except AssertionError as a:
            self.driver.get_screenshot_as_file(picture_path.format(a, timestamp))
            raise a


if __name__ == '__main__':
    unittest.main()
