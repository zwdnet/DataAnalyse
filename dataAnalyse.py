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