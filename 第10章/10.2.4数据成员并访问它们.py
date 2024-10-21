class Geese:
    '''雁类'''
    neck = "脖子较长"
    wing = "振翅频率高"
    leg = "腿位于身体的中心支点，行走自如"

    def __init__(self):
        print("我属于雁类！我有以下特征：")
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)


geese = Geese()
