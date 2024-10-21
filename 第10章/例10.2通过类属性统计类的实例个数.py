class Geese:
    '''雁类'''
    neck = "脖子较长"
    wing = "振翅频率高"
    leg = "腿位于身体的中心支点，行走自如"
    number = 0
    def __init__(self):
        Geese.number += 1
        Geese.beak = '喙的基部较高，长度和头部的长度几乎相等'
        print("\n我是第" + str(Geese.number) + "只大雁，我属于雁类！我有以下特征：")
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)

list1 = []
for i in range(4):
    list1.append(Geese())

print('一共有' + str(Geese.number) + '只大雁')
print('第2只大雁的喙：', list1[1].beak)
geese = Geese()