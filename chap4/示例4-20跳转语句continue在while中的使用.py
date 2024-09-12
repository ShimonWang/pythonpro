s = 0
i = 1
while i <= 10:
    if i%2:
        i += 1
        continue
    s += i
    i += 1
print('1-100之间的偶数和是：', s)