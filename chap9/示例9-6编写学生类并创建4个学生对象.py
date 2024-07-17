class Student:
    # 类属性：定义在类中，方法外的变量
    school = '北京xxx教育'

    # 初始化方法
    def __init__(self, xm, age):
        self.name = xm
        self.age = age

    # 定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫：{self.name}，今年：{self.age}岁了')


# 根据“图纸”可以创建N多个对象
stu = Student('王涛', 23)
stu2 = Student('陈梅梅', 20)
stu3 = Student('马丽', 21)
stu4 = Student('Mary', 23)

print(type(stu))
print(type(stu2))
print(type(stu3))
print(type(stu4))
print(Student.school)

Student.school = '派森教育'
lst = [stu, stu2, stu3, stu4]
for item in lst:
    item.show()
    print(item)
    print(type(item))
