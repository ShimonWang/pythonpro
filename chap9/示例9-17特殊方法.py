a = 10
b = 20
print(dir(a))
print(a+b)
print(a.__add__(b))
print(a.__sub__(b))
print(f'{a}<{b}吗', a.__lt__(b))
print(f'{a}<={b}吗', a.__le__(b))
print(f'{a}=={b}吗', a.__eq__(b))
print('-'*40)
print(f'{a}>{b}吗', a.__gt__(b))
print(f'{a}>={b}吗', a.__ge__(b))
print(f'{a}!={b}吗', a.__ne__(b))
print('-'*40)
print(a.__mul__(b))
print(a.__truediv__(b))
print(a.__mod__(b))
print(a.__floordiv__(b))

