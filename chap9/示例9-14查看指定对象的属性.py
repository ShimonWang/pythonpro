class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫：{self.name}，我今年：{self.age}岁了')


per = Person('陈梅梅', 20)
print(dir(per))
print(per)
