import pandas as pd  # 导入pandas模块
import matplotlib.pyplot as plt  # 导入matplotlib.pyplot模块

# 创建数据
df = pd.DataFrame({'日期': ['9月1日', '9月2日', '9月3日', '9月4日', '9月5日', '9月6日', '9月7日', '9月8日', '9月9日'],
                   '销售数量': [29, 31, 33, 34, 35, 37, 36, 32, 30],
                   '销售金额': [2880, 2980, 3100, 2850, 3212, 3180, 2830, 3200, 3090]})
# 设置x轴和两个y轴的数据
x = df['日期']
y1 = df['销售金额']
y2 = df['销售数量']
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置画布大小
fig = plt.figure(figsize=(8, 5))
# 创建子图表
ax1 = fig.add_subplot(111)
# 第一个折线图
ax1.plot(x, y1, color='red')
# 第一个y轴标签
ax1.set_ylabel('销售金额')
# 第二个折线图
# 共享x轴添加一条y轴
ax2 = ax1.twinx()
ax2.plot(x, y2, color='blue')
# 第二个y轴标签
ax2.set_ylabel('销售数量')
# 销售金额文本标签
for a, b in zip(x, y1):
    ax1.text(a, b, b)
# 销售数量文本标签
for a, b in zip(x, y2):
    ax2.text(a, b + 0.2, b)

plt.show()  # 显示图表
