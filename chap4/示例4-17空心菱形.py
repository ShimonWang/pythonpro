row = eval(input('请输入菱形的行数：'))
while row%2 == 0:
    print('请重新输入菱形的行数:')
    row = eval(input('请输入菱形的行数：'))

top_row = (row+1)//2

for i in range(1, top_row+1):
    for j in range(1, top_row-i+1):
        print(' ', end='')
    for k in range(1, 2*i-1+1):
        if k == 1 or k == 2*i-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

bottom_row = row//2

for i in range(1, bottom_row+1):
    for j in range(1, i+1):
        print(' ', end='')
    for k in range(1, 2*(bottom_row-i)+1+1):
        if k == 1 or k == 2*(bottom_row-i)+1:
            print('*', end='')
        else:
            print(' ', end='')
    print()