a = 100

def calc(x, y):
    return a+x+y

print(a)
print(calc(10, 20))
print('-'*30)

def calc2(x, y):
    a = 200
    return a+x+y

print(calc2(10, 20))
print(a)

def calc3(x, y):
    global s
    s = 300
    return s+x+y

print(calc3(10, 20))
print(s)