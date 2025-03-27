s = 'HelloWorld'
new_s = s.replace('o', '你好')
print(new_s)

print(s.center(20))
print(s.center(20, '*'))

s = '      Hello     World       '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s3 = 'dl-HelloWorld'
print(s3.strip('ld'))
print(s3.strip('oW'))
print(s3.strip('dl-H'))
print(s3.lstrip('ld'))
print(s3.lstrip('dlHello'))