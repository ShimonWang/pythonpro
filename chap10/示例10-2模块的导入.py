import my_info
print(my_info.name)
my_info.info()

import my_info as a
print(a.name)
a.info()

# from my_info import name
# print(name)
# # info()
#
# from my_info import info
# info()

from my_info import *

print(name)
info()

