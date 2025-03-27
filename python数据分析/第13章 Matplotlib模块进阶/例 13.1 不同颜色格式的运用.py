import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0.0, 2.0, 201)
s = np.sin(2*np.pi*t)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码问题
plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示问题
fig, ax = plt.subplots(facecolor=(.18, .31, .31))  # RGB元组
ax.set_facecolor('#eafff5')  # 十六进制字符串
ax.set_title('电压与时间图表', color='0.7')  # 灰度值字符串
ax.set_xlabel('时间(s)', color='c')
ax.set_ylabel('电压(mV)', color='peachpuff')
ax.plot(t, s, 'xkcd:crimson')
ax.plot(t, .7*t, color='C4', linestyle='--')
ax.tick_params(labelcolor='tab:orange')
plt.show()
