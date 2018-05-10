# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/5/9 13:41

from selenium import webdriver

#加载配置文件，免登录
profilepath=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\01qd1l7g.default"
profile=webdriver.FirefoxProfile(profilepath)
driver=webdriver.Firefox(profile)

driver.get("https://i.cnblogs.com/EditPosts.aspx?opt=1")
js_richtext1="document.getElementById('Editor_Edit_EditorBody_ifr').contentWindow.document.body.innerHTML='hhh111'"
js_richtext2="document.getElementById('Editor_Edit_EditorBody_ifr').contentWindow.document.getElementById('').innerHTML='hhh111'"
driver.execute_script(js_richtext1)