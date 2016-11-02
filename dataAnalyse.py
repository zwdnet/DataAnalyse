# -*- coding:utf-8 -*-
#读入csv文件，进行数据分析
import pandas as pd

df = pd.read_csv('money.csv', encoding = 'gbk')
print(df[:3])

#数据处理
import matplotlib.pyplot as plt
# plt.plot(df['Amount'])
# plt.show()

#收入
Income = []
#支出
Outcome = []
for i in df["Amount"]:
    if i < 0:
        Outcome.append(abs(i))
        Income.append(0)
    elif i > 0:
        Income.append(i)
        Outcome.append(0)
    else:
        pass

plt.plot(Income)
plt.plot(Outcome)
plt.show()

#计算累积收入支出
accumuIncome = []
accumuOutcome = []
i = 0
for data in Income:
    if i == 0:
        accumuIncome.append(data)
    else:
        accumuIncome.append(data + accumuIncome[i-1])
    i += 1
#收入与支出的差额
sub = []
i = 0
for data in Outcome:
    if i == 0:
        accumuOutcome.append(data)
    else:
        accumuOutcome.append(data + accumuOutcome[i-1])
    sub.append(accumuIncome[i] - accumuOutcome[i])
    i += 1
plt.plot(accumuIncome)
plt.plot(accumuOutcome)
plt.plot(sub)
plt.show()

#将数据按类型分组
grouped = df['Amount'].groupby(df['TypeName'])
result = abs(grouped.sum())
num = []
for d in result:
    num.append(d)

# import pylab as pl
# pl.hist(num, bins = 1)
# pl.show()

plt.plot(num)
plt.show()

#print(df.dtypes)

#按月分组
i = 0
Time = []
for time in df['Time']:
    #df['time'][0].values = int(time)
    #print(int(time))
    Time.append(int(time/100))
    i += 1

#将原始数据转换为时间按月的数据
df_month = df
df_month['Time'] = Time
print(df_month[:3])
#按月份分组，计算每个月的纯收入
grouped = df_month['Amount'].groupby(df_month['Time'])
result = grouped.sum()
#print(result)
num = []
for d in result:
    num.append(d)
plt.plot(num)
plt.show()

#按年分组
i = 0
Time = []
for time in df_month['Time']:
    Time.append(int(time/100))
    i += 1

#将原始数据转换为时间按年的数据
df_year = df
df_year['Time'] = Time
print(df_year[:3])
#按月份分组，计算每年的纯收入
grouped = df_year['Amount'].groupby(df_year['Time'])
result = grouped.sum()
# print(result)
num = []
for d in result:
    num.append(d)
plt.plot(num)
plt.show()
