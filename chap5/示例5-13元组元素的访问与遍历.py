t = ('python', 'hello', 'world')
print(t[0])
t2 = t[0:3:2]
print(t2)

for item in t:
    print(item)

for i in range(len(t)):
    print(i, t[i])

for index,item in enumerate(t):
    print(index, '------>', item)

for index,item in enumerate(t, start=11):
    print(index, '------>', item)