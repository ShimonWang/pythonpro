class Person():
    def eat(self):
        print("人，吃五谷杂粮")


class Cat():
    def eat(self):
        print("猫，喜欢吃鱼")


class Dog():
    def eat(self):
        print("狗，喜欢啃骨头")


def fun(obj):
    obj.eat()

per = Person()
cat = Cat()
dog = Dog()

#调用fun函数
fun(per)
fun(cat)
fun(dog)