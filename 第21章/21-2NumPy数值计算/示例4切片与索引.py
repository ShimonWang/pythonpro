import numpy as np
# a = np.arange(10)
# print(a)
# print(a[3])
# print(a[2:5:2])
# print(a[2:5])
# print(a[2:])
# print(a[:5])
# print(a[-2])
# a[1] = 2
# print(a)


a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('a', a)
print('a[1]', a[1])
print('a[1:]', a[1:])
print('a[0,1:4]', a[0,1:4])
print('a[...,1]', a[...,1])
print('a[1,...]', a[1,...])
print('a[...,1:]', a[...,1:])
print(a[0][1])
print(type(a[0]))
print(type(a[0][1]))