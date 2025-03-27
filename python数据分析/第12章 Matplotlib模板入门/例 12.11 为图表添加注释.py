import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler


dates = ['1日', '2日', '3日', '4日', '5日',
         '6日', '7日', '8日', '9日', '10日',
         '11日', '12日', '13日', '14日']
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('体温.xls')
x = df['日期']
y = df['体温']
# plt.plot(x,y)
plt.plot(x, y, color='m', linestyle='-', marker='o', mfc='w')
plt.xlabel('2023年1月')
plt.ylabel('基础体温')
plt.tick_params(bottom=True, left=True, right=True, top=True)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.xticks(range(1, 15, 1), dates)
plt.yticks(np.arange(34.4, 38, 0.2))

for a, b in zip(x, y):
    plt.text(a, b, '%.1f' % b, ha='center', va='bottom', fontsize=9)
plt.legend(('基础体温',), loc='upper right', fontsize=10, frameon=False)
plt.annotate('最高体温', xy=(9, 37.1),
             xytext=(10.5, 37.3),
             xycoords='data',
             arrowprops=dict(facecolor='r', shrink=0.05))
plt.grid(color='0.5', linestyle='--', linewidth=1)
plt.show()
