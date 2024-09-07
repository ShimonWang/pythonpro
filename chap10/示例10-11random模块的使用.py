import random

random.seed(10)
print(random.random())
print(random.random())
print('-' * 40)
random.seed(0)
print(random.randint(1, 10))

for i in range(10):
    print(random.randrange(1, 10, 3))

print(random.uniform(1, 100))

lst = [i for i in range(1, 11)]
print(random.choice(lst))
print(lst)
lst1 = [1, 2, 3, 4]
print(lst1)
print(type(lst1))

random.shuffle(lst)
print(lst)

random.shuffle(lst)
print(lst)
