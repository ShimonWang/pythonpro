#!/usr/bin/python3

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
list3 = list1
print ("list2 列表: ", list2)
print(dir(list2))
print(id(list1))
print(id(list2))
print(id(list3))