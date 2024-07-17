class Student():
    # 首尾双下划线
    def __init__(self, name, age, gender):
        self._name = name
        self.__age = age
        self.gender = gender

    def _fun1(self):
        print('子类及本身可以访问')

    def __fun2(self):
        print('只有定义的类可以访问')

    def show(self):
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)


# 创建一个学生类的对象
stu = Student('陈梅梅', 20, '女')
# 类的外部
print(stu._name)
# print(stu.__age)

# 调用受保护的实例方法
stu._fun1()
# 私有方法
# stu.__fun2()

# 私有的实例属性和方法是真的不能访问吗？
print(stu._Student__age)

stu._Student__fun2()

print(dir(stu))