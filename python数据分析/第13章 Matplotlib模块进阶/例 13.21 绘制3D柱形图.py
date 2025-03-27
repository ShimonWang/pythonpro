import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
zs = [1,5,10,15,20]
ax = fig.add_subplot(projection='3d')
for z in zs:
    x = np.arange(0,10)
    y = np.random.randint(0,30, size=10)
    ax.bar(x, y, zs=z, zdir='x', color=['r', 'green', 'yellow', 'c'])

plt.show()