import sys

for line in sys.stdin:
    try:
        a = line.split()
        print(f"type(line):{type(line)},{line}")
        print(f"type(a):{type(a)}, {a}")
        if len(a) >= 2:
            print(int(a[0]) + int(a[1]))
        else:
            print("每行必须输入超过两个数字")
    except ValueError:
        print("输入无效，无法转换为整数")


# 牛客官方
# ----------------------------------------------------------------------------------------------------------------------
# import sys
#
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))


#
# ----------------------------------------------------------------------------------------------------------------------
# import sys
# # data = sys.stdin.read().strip().split()
# # print(f"sys.stdin:{sys.stdin}")
# # print(f"sys.stdin.read():{sys.stdin.read()}")
# # print(f"sys.stdin.read().strip():{sys.stdin.read().strip()}")
# # print(f"sys.stdin.read().strip().split():{sys.stdin.read().strip().split()}")
#
# data = """1 2
# 3 4"""
# print(f"sys.stdin:{data}")
# print(f"sys.stdin.read():{data.read()}")
# print(f"sys.stdin.read().strip():{sys.stdin.read().strip()}")
# print(f"sys.stdin.read().strip().split():{sys.stdin.read().strip().split()}")