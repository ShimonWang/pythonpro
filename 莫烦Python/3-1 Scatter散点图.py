import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
C = np.arctan2(Y,X)

plt.scatter(X,Y,s=75,c=C,alpha=0.5)

plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xticks([])
plt.yticks([])

plt.show()