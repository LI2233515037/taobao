"""网址"""
from selenium.webdriver.common.by import By

taobao = "https://www.taobao.com/"
jing_dong = "https://www.jd.com/"

"""首页"""
search = By.ID, "q"  # 搜索框
search_button = By.CSS_SELECTOR, '[type="submit"]'  # 搜索按钮

"""商品列表页"""
commodity = By.ID, 'J_Itemlist_TLink_654578360475'  # 列表页商品

"""商品详情页"""
color_of_body = By.CSS_SELECTOR, '[title="{}"]'  # 机身颜色
memory_capacity = By.CSS_SELECTOR, '[title="{}"]'  # 存储容量

cookies = [
    {'domain': '.taobao.com', 'expiry': 1693383410, 'httpOnly': False, 'name': 'l', 'path': '/', 'secure': False,
     'value': 'fBx7IVl7NQUJxsZBBOfaFurza77OSIRYYuPzaNbMi9fP91CB5oGGW1GfAyY6C3GcF68HR3VZC7jvBeYBqQAonxvtIosM_CkmndLHR35..'},
    {'domain': '.taobao.com', 'expiry': 1693383410, 'httpOnly': False, 'name': 'tfstk', 'path': '/', 'secure': False,
     'value': 'c5wRB-a2pZboLq7n3YCDTCB5Tt7GwpQKl3gHpR8PxTx4-q1mTR2Th55SAVuRD'},
    {'domain': '.taobao.com', 'expiry': 1693383405, 'httpOnly': False, 'name': 'isg', 'path': '/', 'secure': False,
     'value': 'BAwM1JtvhF7ONpAiul9UX5T33Wo-RbDvhbrwPGbNBbda8az7jledfKRDlfhJvehH'},
    {'domain': '.taobao.com', 'httpOnly': False, 'name': 'uc1', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'cookie21=URm48syIZJwcbRltXU0bIA%3D%3D&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0&existShop=false&cookie14=UoezSH%2FEc5I2bg%3D%3D'},
    {'domain': '.taobao.com', 'expiry': 1678436206, 'httpOnly': False, 'name': '_m_h5_tk_enc', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '7f006301f02cb4e2ff0ca4fbe35322fe'},
    {'domain': '.taobao.com', 'expiry': 1678436206, 'httpOnly': False, 'name': '_m_h5_tk', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '38942ba9740de3a2705c177c70c7c15a_1677838967031'},
    {'domain': '.taobao.com', 'httpOnly': False, 'name': 'dnk', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '%5Cu5384%5Cu739B%5Cu5974%5Cu80332233515037'},
    {'domain': '.taobao.com', 'httpOnly': False, 'name': 'cancelledSubSites', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': 'empty'},
    {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie1', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'BxFmh9%2F586%2B95oOJmLcKsMSqE0QM9BBxYh%2FU%2BfYVQlk%3D'},
    {'domain': '.taobao.com', 'httpOnly': False, 'name': '_l_g_', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'Ug%3D%3D'},
    {'domain': '.taobao.com', 'httpOnly': False, 'name': '_nk_', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '%5Cu5384%5Cu739B%5Cu5974%5Cu80332233515037'},
    {'domain': '.taobao.com', 'httpOnly': False, 'name': 'existShop', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'MTY3NzgzMTQwNg%3D%3D'},
    {'domain': '.taobao.com', 'httpOnly': False, 'name': 'csg', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '78a409ef'},
    {'domain': '.taobao.com', 'expiry': 1680452205, 'httpOnly': True, 'name': 'uc3', 'path': '/', 'sameSite': 'None',
     'secure': True,
     'value': 'lg2=UtASsssmOIJ0bQ%3D%3D&nk2=1Q%2BqhfqPK7Jy%2FE0C6hEwRHGK&vt3=F8dCsfbZb9iYgzBesMo%3D&id2=UU6hQma%2FuL%2BgDg%3D%3D'},
    {'domain': '.taobao.com', 'httpOnly': True, 'name': 'unb', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '2606744410'},
    {'domain': '.taobao.com', 'expiry': 1678465006, 'httpOnly': False, 'name': 'mt', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': 'ci=31_1'},
    {'domain': '.taobao.com', 'httpOnly': False, 'name': 'sg', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '70e'},
    {'domain': '.taobao.com', 'expiry': 1680452205, 'httpOnly': False, 'name': 'lgc', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': '%5Cu5384%5Cu739B%5Cu5974%5Cu80332233515037'},
    {'domain': '.taobao.com', 'httpOnly': True, 'name': 'skt', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '2f12bebfd9b43739'},
    {'domain': '.taobao.com', 'expiry': 1680452205, 'httpOnly': True, 'name': 'uc4', 'path': '/', 'sameSite': 'None',
     'secure': True,
     'value': 'id4=0%40U2xsApNzI3v0fodMSl3KCHvUTy6L&nk4=0%4019OHqLsswNGGAwsL4Oq915vs8TLzLCFM5PA4pl4%3D'},
    {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie2', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '1001f306c248380ea98b62c21b58e5da'},
    {'domain': '.taobao.com', 'expiry': 1709396205, 'httpOnly': True, 'name': 'sgcookie', 'path': '/',
     'sameSite': 'None', 'secure': True,
     'value': 'E100IWt9vtxqEtBtRbidyPTUQ5EPRuho20mWNS3wztI5MHi5mfIAxguVlPDZN%2Fcj3md5gcCRvhBJPgrbpixjhs2KVvPA1kBNn%2B%2Fzv4j8c9kFXQg%3D'},
    {'domain': '.taobao.com', 'expiry': 1709396205, 'httpOnly': False, 'name': '_cc_', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': 'UtASsssmfA%3D%3D'},
    {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie17', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'UU6hQma%2FuL%2BgDg%3D%3D'},
    {'domain': '.taobao.com', 'expiry': 1677917800, 'httpOnly': False, 'name': 'xlly_s', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '1'},
    {'domain': '.taobao.com', 'httpOnly': True, 'name': '_samesite_flag_', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': 'true'},
    {'domain': '.taobao.com', 'expiry': 1709396205, 'httpOnly': False, 'name': 'tracknick', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '%5Cu5384%5Cu739B%5Cu5974%5Cu80332233515037'},
    {'domain': '.taobao.com', 'expiry': 1709367406, 'httpOnly': False, 'name': 'thw', 'path': '/', 'secure': False,
     'value': 'cn'},
    {'domain': '.taobao.com', 'expiry': 1712391396, 'httpOnly': False, 'name': 'cna', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': '5JqIHGBXMWMCAW/JlqG1rNfO'},
    {'domain': '.taobao.com', 'httpOnly': False, 'name': '_tb_token_', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'efd85a4084e1b'},
    {'domain': '.taobao.com', 'expiry': 1685636205, 'httpOnly': False, 'name': 't', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': '6e5e7182dc8be0770cba259541ef425a'}]
