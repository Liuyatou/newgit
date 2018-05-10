# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/4/29 8:51


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Base():
    def __init__(self,driver):
        self.driver=driver
        self.timeout=15 #查询多少秒
        self.poll=0.5 # 查询时间
    def findeElement(self,loctor):
        element=WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x:x.find_element(*loctor))
        return element


    def findElementNew(self,loctor):#此处loctor为元组
        #找到了返回element，没找到抛异常timeout
        element=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_element_located(loctor))
        return element

    def findElementsNew(self,loctor):#此处loctor为元组
        #找到了返回list 没找到抛异常timeout
        elements=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_all_elements_located(loctor))
        return elements

    def sendKeys(self,loctor,text):
        """
        搜索的关键字
        """
        ele=self.findeElement(loctor)
        ele.send_keys(text)

    def click(self,loctor):

        ele=self.findeElement(loctor)
        ele.click()

    def clear(self,loctor):
        ele=self.findeElement(loctor)
        ele.clear()


    def moveToElement(self,loctor):
        """ 鼠标悬停事件"""
        mos=self.findeElement(self,loctor)
        ActionChains(driver).move_to_element(mos).perform()

    def is_text_in_element(self,loctor,text):
        """判断给定的text在这个元素的文本上，要么返回ture,要么返回false,不让它抛异常"""
        try:
            result= WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element(loctor,text))
            return result
        except:
            return False


    def is_value_in_element(self,loctor,value):
        """判断给定的value在这个元素的文本上，要么返回true，要么返回false，不要让它抛异常
        三种情况为假：0，"",None
        1.找不到元素返回false
        2.value为空返回false
        3.value不在元素的value值离返回false
        """

        try:
            result= WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element_value(loctor,value))
            return result
        except:
            return False

    def is_element_exist(self,loctor):
        """查找元素的时候，存在就返回element,不存在就返回timeout异常"""
        try:
            self.findeElement(loctor)
            return True
        except:
            return False

    def is_alert_exist(self,timeout=5):
        """语文老是教的：直到。。。才。。。
        如果有alert，返回的是alert对象
        没有就返回false
        """
        alert=WebDriverWait(self.driver,timeout,self.poll).until(EC.alert_is_present)
        return alert
    def js_scroll_end(self):
        """滚动至底部"""
        js_height="window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js_height)


    def js_focus(self,loctor):
        """聚焦元素"""
        targe=self.findeElement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoView();",targe)



    def js_scroll_top(self):
        """回到顶部"""
        js="window.scrollTo(0,0)"
        self.driver.execute_script(js)

if __name__ == '__main__':

    driver=webdriver.Firefox()
    base=Base(driver)
    driver.get("http://www.cnblogs.com/yoyoketang/p/")
    import time
    time.sleep(3)

    plun=("xpath","//h3[text()='最新评论']")
    base.js_focus(plun)



    # time.sleep(3)
    # base.js_scroll_end()


    # loc001=("id","kw") #定位百度的搜索框
    # base.sendKeys(loc001,u"哈哈哈")
    #
    # loc002=("css selector","#su") #定位搜索按钮
    # base.click(loc002)

    # news=("xpath","//*[text()='新闻']")#新闻
    # res=base.is_text_in_element(news,u"hhh新")
    # print res












    #
    # loc001=("id","kw") #定位百度的搜索框
    # ele1=base.findeElement(loc001)
    # ele1.send_keys("google")
    #
    # loc002=("css selector","#su") #定位搜索按钮
    # ele2=base.findeElement(loc002)
    # ele2.click()