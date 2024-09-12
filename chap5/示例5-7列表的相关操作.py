lst = ['hello', 'world', 'python']
print('原列表', lst, id(lst))

lst.append('sql')
print('增加元素之后', lst, id(lst))

lst.insert(1, 100)
print(lst)

lst.remove('world')
print('删除列表之后的列表：', lst)

print(lst.pop(1))
print(lst)

# lst.clear()
# print(lst, id(lst))

lst.reverse()
print(lst)

new_lst = lst.copy()
print(lst, id(lst))
print(new_lst, id(new_lst))

lst[1] = 'mysql'
print(lst)