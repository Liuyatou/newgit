# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/4/29 9:01
from day9.conmon.base import Base
from selenium.webdriver.support.ui import WebDriverWait

class NewBug(Base):
    """提交BUG页面"""
    test_tab=("xpath",".//*[@id='mainmenu']/ul/li[4]/a") # 测试tab
    bug_anniu=("link text","Bug") #bug按钮
    ti_bug=("xpath",".//*[@id='createActionMenu']/a") #  提bug
    bug_biaoti=("xpath","//div[@class='row-table']/div/div/input") # bug标题
    bug_zhengwen=("class name", "article-content") #bug正文
    save_bug=("xpath",".//form[@id='dataform']/table/tbody/tr[10]/td[2]/button") # 保存
    bug_truck=("class name","chosen-choices") # bug版本
    chose_truck=("css selector",".active-result.highlighted") # 选择bug版本
    save_success_title=("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a") # 保存成功后
    tankuang=("xpath",".//*[@id='openedBuildLabel']")  # 未选bug版本保存后的弹框

    def click_test_tab(self):
        """点击TAB页切换：测试 """
        self.click(self.test_tab)

    def click_bug_anniu(self):
        """点击bug按钮 """
        self.click(self.bug_anniu)

    def click_ti_bug(self):
        """ 点击提bug"""
        self.click(self.ti_bug)

    def input_bug_biaoti(self,text):
        """ 输入bug标题"""
        self.sendKeys(self.bug_biaoti,text)

    def input_bug_zhengwen(self,text):
        """富文本里面输入内容 """
        self.driver.switch_to_frame(1)
        self.sendKeys(self.bug_zhengwen, text)
        self.driver.switch_to_default_content()


    def add_bug_truck(self):
        """影响的版本 """
        self.click(self.bug_truck)
        self.click(self.chose_truck)

    def click_save(self):
        """点击保存 """
        self.click(self.save_bug)

    def get_bug_title(self):
        """获取返回结果 """
        #考虑2种，成功返回什么，失败返回什么
        try:
            t=self.findeElement(self.save_success_title).text

            return t
        except:
            return ""

    def get_truck_text(self):
        """truck为空的时候弹出内容 """
        try:
            t=self.findeElement(self.tankuang).text

            return t
        except:
            return ""



    def is_truck_text_in(self):
        """ """



