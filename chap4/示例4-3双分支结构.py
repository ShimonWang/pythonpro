number = eval(input('请输入您的六位中奖号码：'))

if number == 987654:
    print('恭喜您中奖了！')
else:
    print('您未中本期大奖！')

result = '恭喜您中奖了！' if number == 987654 else '您未中本期大奖！'
print(result)
print('恭喜您中奖了！' if number == 987654 else '您未中本期大奖！')