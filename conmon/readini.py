# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/5/9 18:54

import ConfigParser

conf=ConfigParser.ConfigParser()

conf.read("cfg.ini")
sender=conf.get("email","sender")
print sender

smtp_server=conf.get("email","sender")
print smtp_server






















































