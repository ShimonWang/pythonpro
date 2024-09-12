import time
start = time.time()
s = 0
for i in range(1, 100+1):
    if i%2:
        continue
    s += i
print('1-100之间的偶数和是：', s)
end = time.time()
print('程序运行时间为：%s Seconds'%(end-start))

s = 0
for i in range(1, 100+1):
    if not i%2:
        s += i
print('1-100之间的偶数和是：', s)
