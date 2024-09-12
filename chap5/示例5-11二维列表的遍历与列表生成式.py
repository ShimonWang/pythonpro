lst = [
    ['城市', '环比', '同比'],
    ['北京', 102, 103],
    ['上海', 104, 504],
    ['深圳', 100, 39]
]
print(lst)

for row in lst:
    print(row, end='\t')
    for item in row:
        print(item, end='\t')
    print()

lst2 = [ [j for j in range(5)] for i in range(4)]
print(lst2)