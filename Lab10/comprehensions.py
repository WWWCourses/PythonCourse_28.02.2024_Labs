# ---------------------------------- Mapping --------------------------------- #
# Task: create l2, containing squars of l1 elements

# l1 = [1,2,3,4]
# # Variant 1 = > NOT GOOD
# l2 = list()
# for el in l1:
#     l2.append(el**2)

# print(l2) # [1, 4, 9, 16]

# # Variant 2 with list comprehensions => GOOD:
# l2 = [el**2 for el in l1]
# print(l2)

# Task: map symbols in string to its ascii code
# print( ord('a') )
# string = 'abc'
# codes = [ord(el) for el in string]
# print(codes)

# --------------------------------- Filtering -------------------------------- #
# TASK: create l2, which will contain only evens from l
# l = [1,2,3,4,5]
# # # Variant 1 = > NOT GOOD
# # l2 = list()
# # for el in l:
# #     if el%2==0:
# #         l2.append(el)
# # # Variant 2 with list comprehensions => GOOD:
# l2 = [el for el in l if  el%2==0]
# print(l2)


# ------------------------ TASK: Flatten list of list ------------------------ #
# m = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# Variant 1 = > NOT GOOD
# flatten_m = list()
# for row in m:
#     for el in row:
#         flatten_m.append(el)

# Variant 2 with list comprehensions => GOOD:
# flatten_m = [
#     el for row in m
#        for el in row
# ]
# print(flatten_m) #



# TASK: create list from dict
# d = {'a':1, 'b':2, 'c':3}
# print(d.items())
# l = [k+str(v) for k,v in d.items()]
# print(l) # ['a1', 'b2', 'c3]

# ------------------------- Dictionary comprehension ------------------------- #
# Create dictionry from string and values:
# values = [1,2,3]
# string = 'abc'


# d = {string[idx]:val for idx, val in enumerate(values)}
# print(d)

