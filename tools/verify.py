from base.base_page import BasePage
from tools.get_log import GetLog

log = GetLog.get_log()

class Assert:
    def assrt_equal(self,exp,location):
        element = BasePage().find_element(location)
        try:
            log.info("正在断言...")
            assert exp == element.text
            log.info("断言成功，测试通过")
        except Exception as e:
            log.error("断言失败，异常信息：{}".format(e))
            raise

    def assrt_inculd(self,exp,location):
        element = BasePage().find_element(location)
        try:
            log.info("正在断言...")
            assert exp in element.text
            log.info("断言成功，测试通过")
        except Exception as e:
            log.error("断言失败，异常信息：{}".format(e))
            raise

if __name__ == "__main__":
    pass

