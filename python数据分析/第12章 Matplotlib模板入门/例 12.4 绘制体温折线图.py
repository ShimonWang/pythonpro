import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler


colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
plt.rcParams['axes.prop_cycle'] = cycler(color=colors)
fig = plt.figure(figsize=(5,3), facecolor='yellow')
df = pd.read_excel('体温.xls')
x = df['日期']
y = df['体温']
# plt.plot(x,y)
plt.plot(x, y, color='m', linestyle='-', marker='o', mfc='y')
plt.show()