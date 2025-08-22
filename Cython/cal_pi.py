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
