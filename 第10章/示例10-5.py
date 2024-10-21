class Geese:
    '''雁类'''
    def __init__(self):
        Geese.neck = '脖子较长'


goose1 = Geese()
goose2 = Geese()
goose1.neck = '脖子没有天鹅的长'
print('goose1的neck属性：', goose1.neck)
print('goose2的neck属性：', goose2.neck)
print(Geese.neck)