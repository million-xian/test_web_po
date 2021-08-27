from selenium.webdriver.common.by import By
from tools.get_log import GetLog
from base.base_page import BasePage,BaseHandles

log = GetLog().get_log()
#对象库层
class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        #元素位置
        self.search_button = (By.XPATH,"{}")
        self.search_text = (By.CSS_SELECTOR,"{}")

    #查找元素
    def find_search_button(self,xpath):
        search_button = (self.search_button[0],self.search_button[1].format(xpath))
        return self.find_element(search_button)

    def find_search_text(self,css):
        search_text = (self.search_text[0],self.search_text[1].format(css))
        return self.find_element(search_text)

#操作层
class IndexHandles(BaseHandles):
    def __init__(self):
        self.index_page = IndexPage()

    #操作元素
    def send_search_text(self,search_text_css,text):
        self.input_text(self.index_page.find_search_text(search_text_css),text)

    def click_search_button(self,search_text_xpath):
        self.index_page.find_search_button(search_text_xpath).click()

#业务层
class IndexProxy:
    def __init__(self):
        self.index_handles = IndexHandles()

    #搜索商品
    def search_product(self,search_text_css,text,search_button_xpath):
        try:
            log.info("正在搜索商品")
            self.index_handles.send_search_text(search_text_css,text)
            self.index_handles.click_search_button(search_button_xpath)
        except Exception as e:
            log.error("搜索商品失败，错误信息：{}".format(e))
            raise
