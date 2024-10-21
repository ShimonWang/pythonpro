import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('../datas/books.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']
x = df['年份']
height = df['销售额']
plt.grid(axis='y', which='major')
#x y轴标签
plt.xlabel('年份')
plt.ylabel('线上销售额（元）')
plt.title('2013-2019年线上图书销售额分析图')
plt.bar(x, height, width=0.5, align='center', color='b', alpha=0.5)

for a,b in zip(x, height):
    plt.text(a, b, format(b,','), ha='center', va='bottom', fontsize=9, color='b', alpha=0.9)

plt.legend(df['销售额'])
plt.show()

typex = print(type(x))
