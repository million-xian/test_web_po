import unittest
from selenium.webdriver.common.by import By
from tools.read_yaml import read_yaml
from untils import DriverUtils
from page.index_page import IndexProxy
from tools.verify import Assert

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtils.get_driver()
        cls.index_proxy = IndexProxy()
        cls.verify = Assert()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quit_driver()

    def setUp(self) -> None:
        self.driver.get("https://www.jd.com/")

    def test_search(self):
        index_datas = read_yaml("jd.yaml")["index"]
        searct_text_css = index_datas["search_text_css"]
        search_button_xpath = index_datas["search_button_xpath"]
        assert_location = index_datas["assert"]
        text = index_datas["search_text"]
        #进行搜索
        self.index_proxy.search_product(search_text_css=searct_text_css,text=text,search_button_xpath=search_button_xpath)
        #验证搜索结果
        assert_location = [By.CSS_SELECTOR,"html.jd_retina body div#J_searchWrap.w div#J_crumbsBar.crumbs-bar div.crumbs-nav div.crumbs-nav-main.clearfix div.crumbs-nav-item strong.search-key"]
        self.verify.assrt_inculd(text,assert_location)


if __name__ == "__main__":
    TestSearch().test_search()
    