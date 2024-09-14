s = {10, 20, 30}
s.add(100)
print(s)

# s.remove(20)
# print(s)
#
# s.pop()
# print(s)
#
# s.clear()
# print(s)

for item in s:
    print(item)

for index,item in enumerate(s):
    print(index, '----->', item)

s = {i for i in range(1, 10)}
print(s)

s = {i for i in range(1, 10) if i%2 == 1}
print(s)

