# -*- coding:utf-8 -*-
# 读入csv文件，进行数据分析
import pandas as pd
import numpy as np

df = pd.read_csv('money.csv', encoding='gbk')
# print(df[:3])

# 数据处理
import matplotlib.pyplot as plt
# plt.plot(df['Amount'])
# plt.show()

# 收入
Income = []
# 支出
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

# 计算累积收入支出
accumuIncome = []
accumuOutcome = []
i = 0
for data in Income:
    if i == 0:
        accumuIncome.append(data)
    else:
        accumuIncome.append(data + accumuIncome[i - 1])
    i += 1
# 收入与支出的差额
sub = []
i = 0
for data in Outcome:
    if i == 0:
        accumuOutcome.append(data)
    else:
        accumuOutcome.append(data + accumuOutcome[i - 1])
    sub.append(accumuIncome[i] - accumuOutcome[i])
    i += 1
plt.plot(accumuIncome)
plt.plot(accumuOutcome)
plt.plot(sub)
plt.show()

# 将数据按类型分组
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

# print(df.dtypes)

# 按月分组
i = 0
Time = []
for time in df['Time']:
    # df['time'][0].values = int(time)
    # print(int(time))
    Time.append(int(time / 100))
    i += 1

# 将原始数据转换为时间按月的数据
df_month = df
df_month['Time'] = Time
# print(df_month[:3])
# 按月份分组，计算每个月的纯收入
grouped = df_month['Amount'].groupby(df_month['Time'])
result = grouped.sum()
# print(result)
num = []
for d in result:
    num.append(d)
plt.plot(num)
plt.show()

# 分离出收入和支出，收入>0，支出<0
df_month_income = df_month[df_month['Amount'] > 0]
df_month_outcome = df_month[df_month['Amount'] < 0]
incomeGroup = df_month_income.groupby(df_month_income['Time'])
outcomeGroup = df_month_outcome.groupby(df_month_outcome['Time'])
incomeSum = incomeGroup.sum()
outcomeSum = outcomeGroup.sum()

num1 = []
for d in incomeSum['Amount']:
    num1.append(d)
plt.plot(num1)

num2 = []
for d in outcomeSum['Amount']:
    num2.append(abs(d))
plt.plot(num2)

plt.show()


# 根据收入支出数据做数据拟合,先做多项式拟合
# 先做数据初始化
def initData(values):
    i = 0
    x = []
    y = []
    for val in values:
        x.append(i)
        y.append(val)
        i += 1
    return x, y
# 拟合收入
x, y = initData(num1)
z1 = np.polyfit(x, y, 1)
p1 = np.poly1d(z1)
print(p1)
yvals = p1(x)
plot1 = plt.plot(x, y, "*")
plot2 = plt.plot(x, yvals)
plt.show()

# 拟合支出
x, y = initData(num2)
z2 = np.polyfit(x, y, 1)
p2 = np.poly1d(z2)
print(p2)
yvals = p2(x)
plot1 = plt.plot(x, y, "*")
plot2 = plt.plot(x, yvals)
plt.show()

# 非线性拟合
# from scipy.optimize import leastsq
# x, y = initData(num1)
# p0 = [1, 1]
#
#
# def hyperbola_residuals(p, y, x):
#     return y - x / (p[0]*x+ p[1])
#
#
# def exponet_residuals(p, y, x):
#     return y - p[0]*np.exp(p[1]/x)
#
#
# hyper_plsq = leastsq(hyperbola_residuals, p0, args=(np.reciprocal(y), np.reciprocal(x)))
# exp_plsq = leastsq(exponet_residuals, p0, args=(y, x))
#
#
# def hyper_value(x, p):
#     return x / (p[0]*x+p[1])
#
#
# def exp_value(x, p):
#     return p[0]*np.exp(p[1]/x)
#
#
# plot1 = plt.plot(x, y, "*")
# plot2 = plt.plot(x, hyper_value(x, hyper_plsq[0]), 'gv--')
# plot3 = plt.plot(x, exp_value(x, exp_plsq[0]))
# plt.legend()
# plt.show()

# 按年分组
i = 0
Time = []
for time in df_month['Time']:
    Time.append(int(time / 100))
    i += 1

# 将原始数据转换为时间按年的数据
df_year = df
df_year['Time'] = Time
# print(df_year[:3])
# 按月份分组，计算每年的纯收入
grouped = df_year['Amount'].groupby(df_year['Time'])
result = grouped.sum()
# print(result)
num = []
for d in result:
    num.append(d)
plt.plot(num)
plt.show()

# 分离出收入和支出，收入>0，支出<0
df_year_income = df_year[df_year['Amount'] > 0]
df_year_outcome = df_year[df_year['Amount'] < 0]
incomeGroup = df_year_income.groupby(df_year_income['Time'])
outcomeGroup = df_year_outcome.groupby(df_year_outcome['Time'])
incomeSum = incomeGroup.sum()
outcomeSum = outcomeGroup.sum()

num = []
for d in incomeSum['Amount']:
    num.append(d)
plt.plot(num)

num = []
for d in outcomeSum['Amount']:
    num.append(abs(d))
plt.plot(num)

plt.show()
