class Geese:
    '''雁类'''
    def __init__(self):
        Geese.neck = '脖子较长'
        Geese.wing = '振翅频率高'
        Geese.leg = '腿位于身体的中心支点，行走自如'
        print("我属于雁类！我有以下特征：", self)
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)


geese = Geese()
print(Geese.neck)