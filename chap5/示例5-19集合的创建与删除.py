s = {10, 20, 30, 40}
print(s)

# s = {[10,20], [30,40]}

s = set()
print(s)
print(type(s))
s = {}
print(s, type(s))

s = set('helloworld')
print(s)

s2 = set([10, 20, 30])
print(s)

s3 = set(range(1, 10))
print(s3)

print('max', max(s3))
print('min', min(s3))
print('len', len(s3))

print('9在集合中存在吗？', 9 in s3)
print('9在集合中不存在吗？', 9 not in s3)

del s3
print(s3)
