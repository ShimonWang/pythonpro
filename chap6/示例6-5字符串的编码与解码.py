s = '伟大的中国梦'
scode = s.encode(errors='replace')
print(scode)

scode_gbk = s.encode('gbk', errors='replace')
print(scode_gbk)

# s2 = 'alpha▲▲☺☺☺'
# scode = s2.encode('gbk', errors='strict')
# print(scode)

print(bytes.decode(scode_gbk, 'gbk'))
print(bytes.decode(scode, 'utf-8'))