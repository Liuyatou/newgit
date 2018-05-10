# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/5/8 12:54

import os

#获取当前脚本的路径

print __file__  #(左斜杠)

#右斜杠(#真实路径)
print os.path.realpath(__file__)
real=os.path.realpath(__file__)

#当前脚本的文件夹路径
print os.path.dirname(real)

dirname=os.path.dirname(real)
print dirname

gc=os.path.dirname(dirname)
print gc

#进common
com=os.path.join(gc,"common")
print com

exl=os.path.join(com,"testdata.xlsx")
print exl

















