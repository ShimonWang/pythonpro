# pi = 4(1-1/3+1/5-1/7+1/9-1/11+...)
def calculate_pi(count: int) -> float:
    result = 0.0
    positive = True
    for i in range(count):
        tmp = 1.0 / float(i*2+1)
        if positive:
            result += tmp
        else:
            result -= tmp
        positive = not positive
        
    return result * 4.0

import cython
def calculate_pi_anotated(count: int) -> float:
    result: cython.double = 0.0
    positive: cython.bint = True
    i: cython.int
    for i in range(count):
        tmp: cython.double = 1.0 / float(i*2+1)
        if positive:
            result += tmp
        else:
            result -= tmp
        positive = not positive

    return result * 4.0
