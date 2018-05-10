# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/4/29 8:50

import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from day9.conmon.base import Base

loginurl="http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"

class LoginPage(Base):
    """登录页面"""
    user=("id","account")
    pwd_p=("name","password")
    submit_login=("id","submit")
    zhanghao=("css selector","#userMenu>a")



    # def __init__(self,driver):
    #     self.driver=driver #形参
    #     self.driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")

    def open_login_page(self):
        self.driver.get(loginurl)
    def input_username(self,username):
        """输入账号"""
        self.sendKeys(self.user,username)

    def input_pwd(self,pwd):
        """输入密码"""
        self.sendKeys(self.pwd_p,pwd)

    def click_button(self):
        """点击登录按钮"""
        self.click(self.submit_login)

    def login_in(self,username="admin",pwd="123456"):#定义一个形参
        """登录流程"""
        self.open_login_page()
        self.input_username(username)
        self.input_pwd(pwd)
        self.click_button()

    def is_login_success(self):
        """获取登录的结果"""
        try:
            #获取用户名
            re_text=self.driver.find_element(By.CSS_SELECTOR,"#userMenu>a").text
            print "登录成功"
            return re_text
        except:
            print "登录失败啦"
            return ""

    def is_alert(self):
        '''判断是否有弹窗，有的话点确定，没有的话就pass
        有缺陷：如果页面卡，出现alert慢就判断不到了
        '''
        try:
            alert=self.driver.switch_to_alert() # 这一步不会报错
            print alert.text # 这一步，没有获取到alert文本就报错了
            alert.accept() # 点确定按钮

        except:
            pass

    def is_alert_exits_base(self):
        """
        公共方法
        30s之内循环查找，只要出现就可以接收它，如果没有alert，就等30s后执行
        """
        try:
            alert=self.is_alert_exist()
            alert.accept()
        except:
            pass

    def logout(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()