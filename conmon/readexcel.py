# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/5/7 16:38

import xlrd

#打开excel表格
data=xlrd.open_workbook("testdata.xlsx")
#获取sheet
table=data.sheet_by_name(u"Sheet1")

#行数
nrows=table.nrows
#列数
ncols=table.ncols
print nrows
print ncols
#第一行的搜数据
print table.row_values(0)
#第一列的所有数据
print table.col_values(0)