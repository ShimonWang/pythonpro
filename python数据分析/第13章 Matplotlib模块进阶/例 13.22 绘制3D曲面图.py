import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.arange(-4.0,4.0,0.125)  # stop:区间结束。该区间不包括此值，除非在某些情况下步长不是整数且浮点数舍入影响输出长度。
y = np.arange(-3.0,3.0,0.125)
print(x)
X,Y = np.meshgrid(x,y)
Z1 = np.exp(-X**2-Y**2)
Z2 = np.exp(-(X-1)**2-(Y-1)**2)
Z = (Z1-Z2)*2
ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('rainbow'))
plt.show()