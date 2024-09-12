answer = 'y'
while answer == 'y':
    print('------------欢迎使用10086查询功能------------------')
    print('1.查询当前余额')
    print('2.查询当前剩余流量')
    print('3.查询当前的剩余通话时长')
    print('0.退出系统')
    choice = input('请输入您要执行的操作：')
    if choice == '1':
        print('当前余额为：234.5元')
    elif choice == '2':
        print('当前的剩余流量为：4GB')
    elif choice == '3':
        print('当前的剩余通话时间长为：300分钟')
    elif choice == '0':
        print('程序退出，谢谢您的使用')
        break
    else:
        print('对不起，您输入的有误，请重新输入')
    answer = input('还继续操作吗？y/n')
else:
    print('程序退出，谢谢您的使用')