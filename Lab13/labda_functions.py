
# ----------------------------- lambda functions ----------------------------- #
# def foo(x,y):
#     # print(x,y)
#     return x+y

# bar = lambda x,y: x+y

# print( foo(2,3) )
# print( bar(2,3) )

### Example 1
# def calc(f,x):
#     print(f'Calculating...')
#     return f(x)

# # def cub(x):
# #     return x**3


# # def power(x):
# #     return x**2

# x = 2
# print( calc(lambda x:x**3, x) ) # 8
# print( calc(lambda x:x**2, x) ) # 4
# print(x)  # 2


# ----------------------------- Lambda use cases ----------------------------- #
####### TASK: sort students by math score (ascending)
# students = [
#     {
#         "name": 'Ivan',
#         "math": 5,
#         "physics": 4
#     },
#     {
#         "name": 'Maria',
#         "math": 6,
#         "physics": 3
#     },
#     {
#         "name": 'Petar',
#         "math": 4,
#         "physics": 6
#     }
# ]

# def sort_by_math(student):
#     return student['math']

# students.sort(key=lambda student:student['math'])
# # students =sorted(students)

# print(students) # petar, ivan, mari


######## TASK: filter students by math score > 4
# students = [
#     {
#         "name": 'Ivan',
#         "math": 5,
#         "physics": 4
#     },
#     {
#         "name": 'Maria',
#         "math": 6,
#         "physics": 3
#     },
#     {
#         "name": 'Petar',
#         "math": 4,
#         "physics": 6
#     }
# ]

### Variant 1 => THE WORST:
# filtered = []
# for student in students:
#        if student['math']>4:
#             filtered.append(student)

# print(filtered)

### Variant 2 => with filter()
# filtered = filter( lambda student:student['math']>4, students)
# print(list(filtered))

### Variant 3: List Comprehensions
# filtered = [student for student in students if student['math']>4]
# print(filtered)


####### TASK: map students to student_names
# students = [
#     {
#         "name": 'Ivan',
#         "math": 5,
#         "physics": 4
#     },
#     {
#         "name": 'Maria',
#         "math": 6,
#         "physics": 3
#     },
#     {
#         "name": 'Petar',
#         "math": 4,
#         "physics": 6
#     }
# ]

### Variant 1 => THE WORST:
# student_names = []
# for student in students:
#     student_names.append(student['name'])

# print(student_names)


# ### Variant 2 => with map function:
# student_names = map(lambda student:student['name'],students )
# print(list(student_names))

# ### Variant 3 => with list comprehnsions:
# student_names = [student['name'] for student in students]
# print(student_names)
