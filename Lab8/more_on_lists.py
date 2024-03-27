# ------------------------------- list.insert() ------------------------------ #
# fruits = ['apple', 'banana', 'cherry']

# fruits.insert(1, "orange")
# print(fruits)

# -------------------------------- list.pop()
# -------------------------------- #

# fruits = ['apple', 'banana', 'cherry']
# element = fruits.pop()

# print(fruits)
# print(element)

# ------------------------------- list.remove() ------------------------------ #
# fruits = ['apple-somth','banana', 'cherry']
# try:
#     fruits.remove(1)
# except:
#     print('Element not exists!')

# print( fruits )

# -------------------------------- min/max/sum ------------------------------- #
# l = [1,2,3,4,5]
# print( sum(l) )
# print( min(l) )
# print( max(l) )

# find sum of list elements:
# l = [1,2,3,4,5]
# total_sum = 0

# for el in l:
#     total_sum+=el

# print(total_sum)


# ------------------------------- sorting list ------------------------------- #
### sorted()

# data = [1,2,5,3,4]
# sorted_data = sorted(data, reverse=True)

# print(data)
# print(sorted_data)

### list.sort()

# data = [1,2,5,3,4]
# data.sort(reverse=True) # inplace

# print(data)


# ------------------------------ Loops on lists ------------------------------ #

# l = [1, 2, 3, 1, 4]
# remove all 1s:
# while 1 in l:
#     l.remove(1)

# for _ in l:
#     l.remove(1)

# print(l)


# ----------------------------------- TASK ----------------------------------- #
# ask user to enter 3 student names and their math scores
# Find the student with max score

# students: ivan | stoyan | petar
# scores   :  5  |      3 |    6

# students_scores_1 = [
#     ['ivan', ...],
#     [5, ...]
# ]

# students_scores_2 = [
#     ['ivan', 5],
#     [],
#     [],
# ]

### Get user input
# untill enters ''
# students = []
# scores = list()

# user_input = input('Enter student name ('' for end): ')
# while user_input != '':
#     students.append(user_input)
#     user_input = input('Enter student name ('' for end): ')

# while True:
#     try:
#         input_name = input('Enter student name ('' for end): ').strip()
#         if (not input_name):
#             break
#         input_score = float(input('Enter student score ('' for end): ').strip())
#         if (not input_score):
#             break
#     except ValueError as e:
#         print('Enter a number')
#     except KeyboardInterrupt:
#         print('Buy')
#         exit()
#     except Exception:
#         print('Ups, something went wrong!')

#     students.append(input_name)
#     scores.append(input_score)

# print(students) # ['ivan']
# print(scores) # ['ivan']


### Find best student:
# students=['ivan', 'geogre', 'petar']
# scores = [5,4,6]

# max_score = max(scores)
# print(max_score)  # 6

# max_score_index = scores.index(max_score)
# print(f'Best student is {students[max_score_index]}')












