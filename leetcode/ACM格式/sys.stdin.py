import sys

for line in sys.stdin:
    try:
        a = line.split()
        if len(a) >= 2:
            print(int(a[0]) + int(a[1]))
        else:
            print("每行必须输入超过两个数字")
    except ValueError:
        print("输入无效，无法转换为整数")