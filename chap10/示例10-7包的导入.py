import admin.my_admin as a
a.info()

print('-'*40)
from admin import my_admin as b
b.info()

print('-'*40)
from admin.my_admin import info
my_admin.info()

print('-'*40)
from admin.my_admin import info
from admin import my_admin
my_admin.info()

from admin.my_admin import *
print(name)



