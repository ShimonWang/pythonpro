s = 'helloworldhelloworldhelloworldsasdaksbdjksb'

new_s = ''
for item in s:
    if item not in new_s:
        new_s += item
print(new_s)

new_s2 = ''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2 += s[i]
print(new_s2)

new_s3 = set(s)
lst = list(new_s3)
print(lst)
print('s.index:', s.index)
lst.sort(key=s.index)
print(''.join(lst))