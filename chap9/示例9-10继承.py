class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫:{self.name}，我今年：{self.age}岁了')


per = Person('王涛', 23)
per.show()


# Student继承Person类
class Student(Person):
    def __init__(self, name, age, stunum):
        super().__init__(name, age)
        self.stunum1 = stunum

class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department1 = department

stu = Student('陈梅梅', 20, 1024)
stu.show()

doctor = Doctor('张一一', 32, '外科')
print(doctor.department1)
doctor.show()