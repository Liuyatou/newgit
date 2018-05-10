# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/5/6 15:43

from day9.page.loginpage import LoginPage
from selenium import webdriver
import unittest
import time
import ddt
from day9.conmon.duexcel import ExcelUnit

filepath="E:\\sele_web\\day9\\conmon\\testdata.xlsx"
data=ExcelUnit(filepath)
testdata=data.dict_data()  #读取数据为list
print testdata


# testdata=[
#     {"username":"admin","password":"123456","result":"admin"},
#     {"username":"admin","password":"12345","result":""},
#     {"username":"admin","password":"12345","result":"33"}
#
# ]

@ddt.ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

        cls.loginpage=LoginPage(cls.driver)

    def login_case(self,username,psw):
          #登录

        self.loginpage.login_in(username,psw)
        time.sleep(5)
        #获取结果
        result=self.loginpage.is_login_success()
        #断言
        return result

    @ddt.data(*testdata)
    def test_login_01(self,canshu):
        res=self.login_case(canshu["username"],canshu["password"])
        self.assertTrue(canshu["result"]==res)

    # def test_login_fail(self):
    #     res=self.login_case(can1["username"],can1["password"])
    #     self.assertTrue(can1["result"]==res)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

