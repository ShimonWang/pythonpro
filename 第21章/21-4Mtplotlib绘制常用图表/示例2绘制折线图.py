import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_excel('../datas/data.xlsx')

x1 = df1['姓名']
y1 = df1['语文']
y2 = df1['数学']
y3 = df1['英语']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'in'
plt.title('语数外成绩大比拼', fontsize='18')
plt.plot(x1, y1, label='语文', color='r', marker='p')
plt.plot(x1, y2, label='数学', color='r', marker='.', mfc='r', ms=8, alpha=0.7)
plt.plot(x1, y3, label='英语', color='b', linestyle='-.', marker='*')
plt.grid(axis='y')
plt.ylabel('分数')
plt.yticks(range(50, 150, 10))
plt.legend(['语文', '数学', '英语'])
# plt.show()
# plt.grid(axis='x')
plt.show()