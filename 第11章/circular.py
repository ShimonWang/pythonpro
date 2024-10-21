import math
PI = math.pi
def grith(r):
    '''功能：计算周长
        参数：r（半径）
    '''
    return round(2*PI*r, 2)

def area(r):
    '''
    功能：计算面积
    参数：r（半径）
    :param r:
    :return:
    '''
    return round(PI*r*r, 2)

if __name__ == '__main__':
    print(grith(10))