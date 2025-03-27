import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
# 读取Excel文件
df = pd.read_excel('体温.xls')
# 折线图
x = df['日期']  # x轴数据
y = df['体温']  # y轴数据
plt.plot(x, y, color='m', linestyle='-', marker='o', mfc='w')
plt.xlabel('2023年1月')  # x轴标题
plt.ylabel('基础体温')  # y轴标题
# 计算体温平均值
mean = df['体温'].mean()
plt.axhline(mean, color='red', linestyle='--')

# plt.hlines(mean, xmin=0,xmax=14,colors='r', label="平均体温")
# plt.text(1, mean+0.05, mean, ha ='left', va ='center')
plt.tight_layout()
plt.savefig('image.png')
plt.show()
