i = 0
while i < 3:
    user_name = input('请输入您的用户名：')
    pwd = input('请输入您的密码：')
    if user_name == 'Captain' and pwd == '88888888':
        print('系统正在登录，请稍后')
        i = 4
    else:
        if i < 2:
            print('用户或密码不正确，您还有', 2 - i, '次机会！')
        i += 1

if i == 3:
    print('对不起，三次均输错')
