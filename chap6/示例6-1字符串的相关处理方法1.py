s1 = 'HelloWorld'
new_s2 = s1.lower()
print(s1, new_s2)

new_s3 = s1.upper()
print(new_s3)

e_mail = 'ysj@126.com'
lst = e_mail.split('@')
print('邮箱名：', lst[0], '邮件服务器域名：', lst[1])
print(type(lst))

print(s1.find('o'))
print(s1.find('p'))

print(s1.index('o'))
# print(s1.index('p'))

print('startswith','*'*10)
print(s1.startswith('H'))
print(s1.startswith('P'))

print('endstswith','*'*10)
print('demo.py'.endswith('.py'))
print('text.txt'.endswith('.txt'))


print('HelloWorld'.islower())
print('HelloWorld'.isupper())