import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
A, nu, k = 10, 4, 2
def f(x, A, nu, k):
    return A * np.exp(-k*x) * np.cos(2*np.pi * nu * x)
xmax, nx = 0.5, 8
x = np.linspace(0, xmax, nx)
y = f(x, A, nu, k)
f_nearest = interp1d(x, y,'nearest')
f_linear  = interp1d(x, y,'linear')
f_cubic   = interp1d(x, y,'cubic')
f_next    = interp1d(x, y, 'next')
x2 = np.linspace(0, xmax, 100)
plt.style.use(['science', 'ieee'])
plt.plot(x, y, 'o', label='data points')
plt.plot(x2, f(x2, A, nu, k), label='exact')
plt.plot(x2, f_nearest(x2), label='nearest')
plt.plot(x2, f_linear(x2), label='linear')
plt.plot(x2, f_cubic(x2), label='cubic')
plt.plot(x2, f_next(x2), label='next')
plt.legend(loc=1)
plt.show()
