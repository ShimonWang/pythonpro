import matplotlib.pyplot as plt

# 全局设置字体为Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

desired_order = [
    'a=0.7, b=0.3', 'a=0.5, b=0.5', 'a=0.4, b=0.6', 'a=0.3, b=0.7',
    'a=0.2, b=0.8', 'a=0.1, b=0.9', 'a=0.01, b=0.99'
]
keys = [key for key in desired_order if key in rmse]
values = [rmse[key] for key in keys]

# 将横坐标标签中的'a'和'b'替换为'α'和'β'
keys = [key.replace('a=', 'α=').replace('b=', 'β=') for key in keys]

plt.figure(figsize=(6, 4))

# 创建曲线图
plt.plot(keys,
         values,
         marker='o',
         linestyle='-',
         markersize=8,
         markerfacecolor='b')

# 添加数值标注
for i, value in enumerate(values):
    plt.text(keys[i], value, f'{value:.4f}', ha='center', va='bottom')

# 添加标题和标签
# plt.title('Sensitivity Analysis')
# plt.xlabel('(α, β)')
# plt.ylabel('RMSE')
y_ticks = np.arange(1.5, max(values) + 1, 0.01)
plt.yticks(y_ticks)
plt.ylim(2.06, 2.1)

# 调整x轴刻度位置
plt.xticks(rotation=45, ha='right')

# 显示图形
plt.grid(True)
plt.tight_layout()
plt.show()