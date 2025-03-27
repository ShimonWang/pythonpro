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
plt.xlim(1, 14)
plt.ylim(34, 45)
plt.show()
