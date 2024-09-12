for i in 'hello':
    print(i)

for i in range(1, 11):
    if i%2:
        print(i, '是奇数！')


s = 0
for i in range(1, 11):
    s += i
print('1-10的累加和为：', s)


for i in range(100, 1000):
    unit = i%10
    tens = i//10%10
    hundred = i//10//10%10

    if unit**3 + tens**3 + hundred**3 == i:
        print(i, '是水仙花数')