# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/4/29 16:40

import unittest
from day9.page.loginpage import LoginPage
from day9.page.tibug import NewBug
from selenium import webdriver
import time

class TestNewBug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.newbug=NewBug(cls.driver)
    def add_bug(self,bugtitle,bugdetail):
        """
        新建BUG
        """
        # 1.登录
        self.loginpage.login_in()
        # 2.点测试，bug,提交bug
        self.newbug.click_test_tab()
        self.newbug.click_bug_anniu()
        self.newbug.click_ti_bug()
        # 3.编辑BUG
        self.newbug.input_bug_biaoti(bugtitle)
        self.newbug.input_bug_zhengwen(bugdetail)
        self.newbug.add_bug_truck()
        self.newbug.click_save()
        # 4.获取点完之后的结果
        resul=self.newbug.get_bug_title()
        print resul

        print u"获取实际结果：%s" % resul
        return resul

    def test_add_bug(self):
        nowtime=time.strftime("%Y_%m_%d_%H_%M_%S")
        bugtitle=u"新建一个bug"+nowtime
        bugdetail=u"bug详情"
        re=self.add_bug(bugtitle,bugdetail)

        # 5.期望结果
        ex=bugtitle
        #6.断言
        self.assertEqual(re,ex,msg=u"这句话代表断言失败哈哈哈哈哈")
        self.assertTrue(re==ex)

if __name__ == '__main__':
    unittest.main()






