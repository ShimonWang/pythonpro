# s = lambda a,b:a+b
# print(type(s))
#
# print(s(10, 20))
#
# lst = [10, 20, 30, 40, 50]
# for i in range(len(lst)):
#     print(lst[i])
#
# print()
#
#
# for i in range(len(lst)):
#     result = lambda x:x[i]
#     print(result(lst))

student_scores=[
    {'name':'陈梅梅', 'score':98},
    {'name':'王一一', 'score':95},
    {'name':'张天乐', 'score':100},
    {'name':'白雪儿', 'score':65},
]
# d = dict(student_scores)
# print(d)
student_scores.sort(key=lambda x:x.get('score'), reverse=True)
# student_scores.sort(key=(dict(student_scores)).get('score'), reverse=True)
print(student_scores)