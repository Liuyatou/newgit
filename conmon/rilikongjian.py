# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/5/9 17:58

from selenium import webdriver

driver=webdriver.Firefox()

driver.get("https://kyfw.12306.cn/otn/index/init")

id_="train_date"
js="document.getElementById('%s').removeAttribute('readonly')" %id_

driver.execute_script(js)

driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2018-5-20")