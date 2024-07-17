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
print(stu.name, stu.age)
print(stu2.name, stu2.age)

# 为stu2动态绑定了一个实例属性
stu2.gender = '男'
print(stu2.name, stu2.age, stu2.gender)


# print(stu.gender)
def introduce():
    print('我是一个普通的函数，我被动态绑定成了stu2对象的方法')


stu2.fun = introduce
stu2.fun()
