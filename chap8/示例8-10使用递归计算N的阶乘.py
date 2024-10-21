# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fac(n-1)
#
#
# print(fac(5))

# def xorOperation(n, start):
#     """
#     :type n: int
#     :type start: int
#     :rtype: int
#     """
#     nums = []
#     for i in range(n):
#         nums[i] = start + i * 2
#         if i == 1:
#             nums_XOR = start
#         else:
#             nums_XOR ^= nums[i]
#
#     return nums_XOR
#
# xorOperation(5, 0)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(a))