# import numpy as np
#
# a = np.random.random((1000, 20))
# print(1)
# b = np.arctan2(0, np.pi)
# print(np.pi / 4)
# print(b)
# # np.arctan2

# line2D
import matplotlib.pyplot as plt

# fig = plt.figure()
# fig.suptitle('Figure: sample for Line2D')
# plt.plot([1, 4, 2, 3], linewidth=5)
# plt.show()
plt.show()
line, = plt.plot([1, 4, 2, 3], linewidth=0.5)  # 返回值是一个列表，类似[Line2D实例, ]
line.set_linewidth(0.5)

# np.random.random
import numpy as np
a = np.random.random({5, 2})
print(np.random.random(5))  # 生成[0,1)之间均匀分布的浮点数

# Scipy插值
from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)
#...
from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)


# shape
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
print(x.shape)
print(x.shape(0))


#
import numpy as np
f = np.array([1, 2, 4, 7, 11, 16])
np.gradient(f)
np.gradient(f, 2)

# isinstance
class A:
    pass


class B(A):
    pass


isinstance(A(), A)  # returns True
type(A()) == A  # returns True
isinstance(B(), A)  # returns True
type(B()) == A  # returns False

#
import numpy as np
x = np.array([1, 2, 3])
x1 = x[:, None]
print(type(x))
print(type(x1))
print(type(x[1]))
print(type(x1[1]))
pass
# 原本 x 是形状 (3,) 的一维数组
# 经过操作后，x 变成了形状 (3, 1) 的二维数组
# 结果：
# array([[1],
#        [2],
#        [3]])

# np
import numpy as np
timesteps = 100
x_track = np.zeros(timesteps)  # 创建一个零数组，用于记录每一步的 x 值

# linespace
import numpy as np
a = np.linspace(1, 10, 10)
# b = np.linspace(1,10)
c = np.exp(-1 * a)

# array
import numpy as np
path1 = np.sin(np.arange(0, 1, 0.01) * 5)
# a strange path to target
# 一条通往目标的奇怪路径
path2 = np.zeros(path1.shape)
path2[int(len(path2) / 2.0):] = 0.5
y_des=np.array([path1, path2])
y = [path1, path2]
pass

# 列表切片访问
import numpy as np
c = np.linspace(0, 2 * np.pi, 10 + 1)  # 11个点
type(c)
c1 = c[0:-1]
c2 = c[0:1]
a = list(range(0, 10, 1))
a1 = a[0:-1]
pass

# isnan
import numpy as np

a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(np.nan)
print(np.isnan(a))
a_isnan_index = np.array([True, False, True, False, True, False])
print(type(a_isnan_index))
# print(a[a_isnan_index])
print(~np.isnan(a))
print(type(~np.isnan(a)))
print(a[~np.isnan(a)])
print(a[~a_isnan_index])
pass