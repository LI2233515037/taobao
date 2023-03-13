import time
"""网址"""
from selenium.webdriver.common.by import By

taobao = "https://www.taobao.com/"
tianmao = "https://www.tmall.com/"
jing_dong = "https://www.jd.com/"

"""首页"""
search = By.ID, "key"  # 搜索框
search_button = By.CSS_SELECTOR, '.button'  # 搜索按钮
scroll_bar = "window.scrollTo({},{})"

shopping_trolley_home =By.CSS_SELECTOR,"#settleup"
"""商品列表页"""
commodity = By.CSS_SELECTOR, '[title="{}"]'  # 列表页商品
sort = By.CLASS_NAME,"arrow-bottom"  # 价格排序从低到高

"""商品详情页"""
color_of_body = By.CSS_SELECTOR, '[title="{}"]'  # 机身颜色
memory_capacity = By.CSS_SELECTOR, '[title="{}"]'  # 存储容量
shopping_trolley = By.CSS_SELECTOR, "#InitCartUrl"  # 点击购物车按钮
"""成功加入购物车页面"""
successfully_added_to_cart = By.CLASS_NAME,"ftx-02"#商品已成功加入购物车！
"""购物车页面"""
check_all = By.CSS_SELECTOR,'[name="select-all"]'#全选
to_settle_accounts = By.CLASS_NAME,"common-submit-btn"#去结算
return_to_shopping_cart = By.ID,'cartRetureUrl'#返回修改购物车
delete_product = By.CLASS_NAME,'opt-batch-remove'#删除商品
delete_notarize= By.CLASS_NAME,'no'#确定删除

"""其他"""
picture_path = 'E:\\项目01\\taobao\screenshot\\{}_{}.png'
timestamp = time.strftime("%Y_%m_%d %H_%M_%S")
jd_cookies = [
    {'domain': '.jd.com', 'expiry': 1678260948, 'httpOnly': False, 'name': 'shshshsID', 'path': '/', 'secure': False,
     'value': 'dc4d2d5e0d9552be155dcf169b2baf96_1_1678259148865'},
    {'domain': '.jd.com', 'expiry': 1712819148, 'httpOnly': False, 'name': 'shshshfp', 'path': '/', 'secure': False,
     'value': '39333ee8f4ff037247f6c03e6ff583c4'},
    {'domain': '.jd.com', 'expiry': 1712819148, 'httpOnly': False, 'name': 'shshshfpb', 'path': '/', 'secure': False,
     'value': 'x0rUn9qTvAOb7mH6d27foHQ'},
    {'domain': '.jd.com', 'expiry': 1678863945, 'httpOnly': False, 'name': 'PCSYCityID', 'path': '/', 'secure': False,
     'value': 'CN_110000_110100_0'},
    {'domain': '.jd.com', 'expiry': 1679123145, 'httpOnly': False, 'name': 'areaId', 'path': '/', 'secure': False,
     'value': '1'},
    {'domain': 'www.jd.com', 'expiry': 1709795144, 'httpOnly': False, 'name': 'o2State', 'path': '/', 'secure': False,
     'value': '{%22webp%22:true%2C%22avif%22:true}'},
    {'domain': '.jd.com', 'httpOnly': False, 'name': '__jdc', 'path': '/', 'secure': False, 'value': '76161171'},
    {'domain': '.jd.com', 'expiry': 1678260943, 'httpOnly': False, 'name': '__jdb', 'path': '/', 'secure': False,
     'value': '76161171.3.16782591311701851058624|1.1678259131'},
    {'domain': '.jd.com', 'expiry': 1712819143, 'httpOnly': False, 'name': 'TrackID', 'path': '/', 'secure': False,
     'value': '1bPlMd06jyaK1pNZu_QVxo7mlchmKr7My6By8ZrFWjxTgeyKXIRekWbd-JNd_dTADbMAMAHGkZDLBoeVY4-sr0oThUoSCBTusL_7h5U4feWE'},
    {'domain': '.jd.com', 'expiry': 1680851143, 'httpOnly': False, 'name': 'unick', 'path': '/', 'secure': False,
     'value': '%E4%B8%9B%E6%9E%97%E7%8B%BC002'},
    {'domain': '.jd.com', 'expiry': 1680851143, 'httpOnly': True, 'name': '_pst', 'path': '/', 'secure': False,
     'value': 'wdNNIBOTnNMGzMb'},
    {'domain': '.jd.com', 'expiry': 1680851143, 'httpOnly': False, 'name': '_tp', 'path': '/', 'secure': False,
     'value': 'z0jQndOHCGMaWv4yKmwE4A%3D%3D'},
    {'domain': '.jd.com', 'expiry': 1712819148, 'httpOnly': False, 'name': 'shshshfpa', 'path': '/', 'secure': False,
     'value': 'ad9f98c6-62e9-c465-c435-088c404ec53f-1678259115'},
    {'domain': '.jd.com', 'httpOnly': False, 'name': 'ceshi3.com', 'path': '/', 'secure': False, 'value': '103'},
    {'domain': '.jd.com', 'expiry': 1679123145, 'httpOnly': False, 'name': 'ipLoc-djd', 'path': '/', 'secure': False,
     'value': '1-2901-0-0'},
    {'domain': '.jd.com', 'expiry': 1709795143, 'httpOnly': False, 'name': 'pinId', 'path': '/', 'secure': False,
     'value': 'jmJH8mXtjb1IdVU5o492Eg'},
    {'domain': '.jd.com', 'httpOnly': True, 'name': 'thor', 'path': '/', 'secure': False,
     'value': 'DD80CA713BF121C07B40C26877A361BAEB3CC911CE84B2D87707BB783D4783C3E26960409D21760A2499DF820AAE8E906B72D52045B647F770AF6E3D3FD9E7872EB7BB147BAB631BD9D4B052CC5A82FB392E3CC3F7D283CCDA8D5AC891DE4031CAA27412218A75212CD02A4B69E67EE1F8DD424752FC7859EE5188658FDFFF2FF9D5E6C88EED80F19B593EAB11C44668F9EAB38A9144B0F808D7C67C727A7128'},
    {'domain': '.jd.com', 'expiry': 1693811143, 'httpOnly': False, 'name': '__jda', 'path': '/', 'secure': False,
     'value': '76161171.16782591311701851058624.1678259131.1678259131.1678259131.1'},
    {'domain': '.jd.com', 'expiry': 1693811167, 'httpOnly': False, 'name': '__jdu', 'path': '/', 'secure': False,
     'value': '16782591311701851058624'},
    {'domain': '.jd.com', 'expiry': 1704179149, 'httpOnly': False, 'name': '3AB9D23F7A4B3C9B', 'path': '/',
     'secure': False,
     'value': 'WDX3DUD7ZAMCLLAPKOWONDWLUPWLYVYG2A2ES22TLWZQA2TWIJQD56F4XNVV6X5INZRHGLN2G5G2G4PYHE5KRAZWWY'},
    {'domain': '.jd.com', 'expiry': 1680851143, 'httpOnly': False, 'name': 'pin', 'path': '/', 'secure': False,
     'value': 'wdNNIBOTnNMGzMb'},
    {'domain': '.jd.com', 'expiry': 1712819148, 'httpOnly': False, 'name': 'shshshfpx', 'path': '/', 'secure': False,
     'value': 'ad9f98c6-62e9-c465-c435-088c404ec53f-1678259115'},
    {'domain': '.jd.com', 'expiry': 1679555131, 'httpOnly': False, 'name': '__jdv', 'path': '/', 'secure': False,
     'value': '122270672|direct|-|none|-|1678259131171'}]

tabao_cookies = [
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
tianmao_cookies = [
    {'domain': '.tmall.com', 'expiry': 1693548525, 'httpOnly': False, 'name': 'tfstk', 'path': '/', 'secure': False,
     'value': 'cHlcBmxCkxyjQgdtVmNXtFlxIXtRZYfaxflSaUtmO4I36ScPiHBPLVTXroxB0O1..'},
    {'domain': '.tmall.com', 'expiry': 1678082926, 'httpOnly': False, 'name': 'xlly_s', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': '1'},
    {'domain': '.tmall.com', 'expiry': 1678601324, 'httpOnly': False, 'name': '_m_h5_tk', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '1a14b5a5bfbf44612064905452b16d1f_1678005887376'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': 'uc1', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'existShop=false&pas=0&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=U%2BGCWk%2F7ow08GIhZA1cCPg%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&cookie14=UoezSH5%2F%2BGkEAA%3D%3D'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': 'cancelledSubSites', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': 'empty'},
    {'domain': '.tmall.com', 'httpOnly': True, 'name': 'uc4', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'nk4=0%4019OHqLsswNGGAwsL4Oq915vs8TLzLCFNMoxUnwE%3D&id4=0%40U2xsApNzI3v0fodMSl3KCXOqCXUa'},
    {'domain': '.tmall.com', 'httpOnly': True, 'name': 'sgcookie', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'E100Zpp7RLpTmMPLakgnTZMngQKx4A4x4yUZuK27ol7G6dWQVEiRmMlOMvD6LiKytCjM5f2fAJi%2B5NDtQbXlWuu379SG%2BQhLNUgfvTJavROcrwY%3D'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': 'tracknick', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '%5Cu5384%5Cu739B%5Cu5974%5Cu80332233515037'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': '_nk_', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '%5Cu5384%5Cu739B%5Cu5974%5Cu80332233515037'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': 'sg', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '70e'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': '_tb_token_', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'e81ebeee37e63'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': 'csg', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'aeed761f'},
    {'domain': '.tmall.com', 'httpOnly': True, 'name': 'cookie2', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '106f38838717af4f2562c12c046c284e'},
    {'domain': '.tmall.com', 'expiry': 1712556525, 'httpOnly': False, 'name': 'cna', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': 'wx+LHHP6hwICAW/JlqF29ClX'},
    {'domain': '.tmall.com', 'expiry': 1678601324, 'httpOnly': False, 'name': '_m_h5_tk_enc', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '62ed3d6ecc587f9a08d0feb1c16fdcba'},
    {'domain': '.tmall.com', 'httpOnly': True, 'name': 'cookie1', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'BxFmh9%2F586%2B95oOJmLcKsMSqE0QM9BBxYh%2FU%2BfYVQlk%3D'},
    {'domain': '.tmall.com', 'expiry': 1693548525, 'httpOnly': False, 'name': 'l', 'path': '/', 'secure': False,
     'value': 'fBg4_qvPNOrGmw4CBOfaFurza77tbIRYjuPzaNbMi9fP9pfe5mHdW1G-PoYwCnGcFsf6R3VZC7jvBeYBqIvn3r4AnrZgUSMmne_7Qn5..'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': 'lgc', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '%5Cu5384%5Cu739B%5Cu5974%5Cu80332233515037'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': 'login', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'true'},
    {'domain': '.tmall.com', 'httpOnly': True, 'name': 'uc3', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'id2=UU6hQma%2FuL%2BgDg%3D%3D&lg2=URm48syIIVrSKA%3D%3D&nk2=1Q%2BqhfqPK7Jy%2FE0C6hEwRHGK&vt3=F8dCsfbY5AmzhQQ%2B7pM%3D'},
    {'domain': '.tmall.com', 'expiry': 1693548525, 'httpOnly': False, 'name': 'isg', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': 'BHBwq3Dl4HcXY7xzK3CjMgHGQT7CuVQDQc6ciGrBK0ueJRDPEsoqkFMXeSxFjgzb'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': 'unb', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '2606744410'},
    {'domain': '.tmall.com', 'httpOnly': True, 'name': 'cookie17', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'UU6hQma%2FuL%2BgDg%3D%3D'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': '_l_g_', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': 'Ug%3D%3D'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': 't', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '6e496ce6bd5fddf5699b52d53e1ad7c1'},
    {'domain': '.tmall.com', 'expiry': 1709561324, 'httpOnly': False, 'name': 'lid', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': '%E5%8E%84%E7%8E%9B%E5%A5%B4%E8%80%B32233515037'},
    {'domain': '.tmall.com', 'httpOnly': False, 'name': 'dnk', 'path': '/', 'sameSite': 'None', 'secure': True,
     'value': '%5Cu5384%5Cu739B%5Cu5974%5Cu80332233515037'}]
