import json
lst = [
    {'name':'杨淑娟','age':18,'score':90},
    {'name':'陈梅梅','age':21,'score':99},
    {'name':'张一一','age':19,'score':89}
]

s = json.dumps(lst, ensure_ascii=False, indent=4)
print(type(s))
print(s)


lst2 = json.loads(s)
print(type(lst2))
print(lst2)

# with open('student.txt', 'w') as file:
#     json.dump(lst, file, ensure_ascii=False, indent=4)


with open('student.txt', 'r') as file:
    lst3 = json.load(file)
    print(type(lst3))
    print(lst3)