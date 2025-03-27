import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5,5,1000)
y = [1/(1+np.exp(-i)) for i in x]
plt.plot(x,y)
plt.show()