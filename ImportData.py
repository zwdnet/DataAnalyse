# -*- coding:utf-8 -*-
#导入数据库数据
import sqlite3

#打开数据库
con = sqlite3.connect("money.db")
con.text_factory = lambda x:str(x, 'gb2312')
#取得游标
cu = con.cursor()
#查询
cu.execute("select ID, Time, Name, Amount, TypeName from Income, IncomeType where IncomeType.TypeID == Income.TypeID")
#获取结果
data = cu.fetchall()
#关闭数据库
con.close()

#显示结果
#print(data[10])
#print(cu.description[2][0])
#print(len(data))

#将数据写入csv文件
import csv

with open("money.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    item = []
    for i in range(5):
        item.append(cu.description[i][0])
    writer.writerow(item)
    writer.writerows(data)