# coding:utf-8
# Author:Rola.Yang
# @Time: 2018/5/8 9:53

import xlrd

class ExcelUnit():
    def __init__(self,excelPath,sheetName="Sheet1"):
        #打开excel
        self.data=xlrd.open_workbook(excelPath)
        self.table=self.data.sheet_by_name(sheetName)
        #获取第一行作为key值
        self.keys=self.table.row_values(0)
        #获取总行数
        self.rownum=self.table.nrows
        #获取总列数
        self.colnum=self.table.ncols

    def dict_data(self):
        if self.rownum<=1:
            print u"总行小于1"

        else:
            r=[]
            j=1
            for i in list(range(self.rownum-1)):
                s={}
                #从第二行取对应的values值
                s["rownum"]=i+2
                values=self.table.row_values(j)
                for x in list(range(self.colnum)):
                    # #获取第一行作为key值
                    # self.keys=self.table.row_values(0)
                    s[self.keys[x]]=values[x]
                r.append(s)
                j +=1
            return r
if __name__ == '__main__':
    filepath="testdata.xlsx"
    sheetName="Sheet1"
    data=ExcelUnit(filepath,sheetName)
    print data.dict_data()
    for i in data.dict_data():
        print i


