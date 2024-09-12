# for i in range(1, 9+1):
#     for j in range(1, i+1):
#         print(str(j),'*', str(i), '=', str(i*j), '\t', sep='', end='')
#     print()

for i in range(1, 9+1):
    for j in range(1, i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j), sep='', end='\t')
    print()