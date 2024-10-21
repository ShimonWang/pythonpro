class Swan:
    '''天鹅类'''
    __neck_swan = '天鹅的脖子很长'
    def __init__(self):
        print('__init__():', Swan.__neck_swan)


swan = Swan()
print('加入类名：', swan._Swan__neck_swan)
print('直接访问：', swan.__neck_swan)
