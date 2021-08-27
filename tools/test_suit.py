import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner
from config import BasePath
import os

test_case_path = BasePath+os.sep+"test_cases"

def test_suit(test_cases):
    suit = unittest.TestSuite()
    test = unittest.defaultTestLoader.discover(test_case_path,pattern=test_cases)
    suit.addTests(test)
    now = time.strftime("%Y%m%d %H%M%S",time.localtime())
    report = open(BasePath+os.sep+"report"+os.sep+"report_{}.html".format(now),"wb")
    runner = HTMLTestRunner(stream=report,title="测试报告{}".format(now))
    runner.run(suit)
    report.close()

if __name__ == "__main__":
    test_suit("test*")



