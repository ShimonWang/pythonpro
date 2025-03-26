import matplotlib.pyplot as plt
import numpy as np


def f(x,y):
    return (1 - x/2 + x**5 + y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

plt.contourf(X, Y, f(X,Y), 8, alpha=0.75, cmap="hot")  # 绘制填充等高线
C = plt.contour(X, Y, f(X,Y), 8, colors="black", linewidths=0.5)  # 绘制等高线
plt.clabel(C, inline=True, fontsize=10)  # 为等高线图添加标签 inline:如果 True，则在标签放置的位置移除底层轮廓。

plt.xticks(())
plt.yticks(())
plt.show()
