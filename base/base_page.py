from untils import DriverUtils
from tools.read_yaml import read_yaml

#基类 对象库层
class BasePage:
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        self.black_list = read_yaml("jd.yaml")["balck_list"]

    def find_element(self,location):
        try:
            element = self.driver.find_element(location[0],location[1])
            return element
        except:
            for black in self.black_list:
                element = self.driver.find_element(black[0],black[1])
                if len(element)>0:
                    element[0].click()
                    break
            self.find_element(location)


#基类 操作层
class BaseHandles:
    def input_text(self,element,text):
        element.clear()
        element.send_keys(text)
