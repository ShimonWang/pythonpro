lst = [88, 89, 90, 98, 00, 99]
print(lst)

# for index in range(len(lst)):
#     if lst[index] != 0:
#         lst[index] += 1900
#     else:
#         lst[index] += 2000
#
# print('修改后的年份列表', lst)


for index,value in enumerate(lst):
    if value != 0:
        lst[index] = value + 1900
    else:
        lst[index] = value + 2000

print('修改后的年份列表', lst)