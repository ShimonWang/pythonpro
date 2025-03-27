s = 'helloword'
print('{0:*<20}'.format(s))
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))
print('{0:*<20}'.format(s))

print(s.center(20, '*'))

print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.7865))

print('{0:.2f}'.format(3.1419826))
print('{0:.6}'.format(3.1419826))
print('{0:.5}'.format('helloworld'))

a = 425
print('二进制：{0:b},十进制：{0:d},八进制：{0:o},十六进制：{0:x},十六进制：{0:X}'.format(a))

b = 3.1415926
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))