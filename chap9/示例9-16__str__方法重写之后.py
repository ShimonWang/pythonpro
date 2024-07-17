class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return '这是一个人类，具有name和age两个实例属性'


per = Person('陈梅梅', 20)
print(per)
print(per.__str__())