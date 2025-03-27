import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,360)
y = np.sin(x*np.pi/180)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x,y)
plt.title("正弦函数图像")
plt.show()
