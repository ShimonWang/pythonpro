# s = 'HelloWorld'
# print('e' in s)
# # print(e in s)
# print('v' not in s )
#
# print(len(s))
# print(max(s))
# print(min(s))
# print()
# print(s.count('o'))
s = 'helloworld'
print('e在helloworld中存在吗?', ('e' in s))
print('v在helloworld中存在吗?', ('v' in s))

print('e在helloworld中存在吗?', ('e' not in s))
print('v在helloworld中存在吗?', ('v' not in s))

print('len():', len(s))
print('max()', max(s))
print('min()', min(s))

print('s.index():', s.index('o'))
# print('s.index()', s.index('v'))
print('s.count()', s.count('o'))