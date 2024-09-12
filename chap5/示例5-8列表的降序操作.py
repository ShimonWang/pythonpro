lst = [4, 56, 3, 78, 40, 56, 89]
print('原列表：', lst)

lst.sort()
print('升序', lst)
# print(lst.sort())

lst.sort(reverse=True)
print('降序', lst)

print('-----------------------------')
lst2 = ['banana', 'apple', 'Cat', 'Orange']
print('原列表', lst2)

lst2.sort()
print('升序', lst2)

lst2.sort(reverse=True)
print('降序：', lst2)

lst2.sort(key=str.lower)
print(lst2)