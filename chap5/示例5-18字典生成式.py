import random
d = {item:random.randint(1, 100) for item in range(4)}
print(d)

lst = [1001, 1002, 1003]
lst2 = ['陈梅梅', '王一一', '李丽丽']
d = {key:value for key,value in zip(lst, lst2)}
print(d) 