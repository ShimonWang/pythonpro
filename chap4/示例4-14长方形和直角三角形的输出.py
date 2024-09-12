# for i in range(1, 4):
#     print('*'*4)

# for i in range(1, 4):
#     for j in range(1, 5):
#         print('*', end='')
#     print()

# for i in range(1, 6):
#     print('*'*(i))
#
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print('*', end='')
#     print()

# for i in range(1, 6):
#     print('*'*(6-i))
#
# for i in range(1, 6):
#     for j in range(1, 6-i+1):
#         print('*', end='')
#     print()
'''

&&&&*
&&&***
&&*****
&*******
*********

'''

for i in range(1, 5+1):
    for j in range(1, 5-i+1):
        print(' ', end='')
    for k in range(1, 2*i-1+1):
        print('*', end='')
    print()

for i in range(1, 6):
    for j in range(1, 7-i):
        print(' ', end='')
    for k in range(1, 2*i):
        print('*', end='')
    print()
