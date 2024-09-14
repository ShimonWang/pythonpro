d = {'hello':10, 'world':20, 'python':30}
print(d['hello'])

print(d.get('hello'))

# print(d['java'])
print(d.get('java'))

for item in d.items():
    print(item)

for key,value in d.items():
    print(key, '------>', value)
