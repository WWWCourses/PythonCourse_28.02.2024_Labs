# ----------------------------- Tuple Declaration ---------------------------- #
# t1 = (1,2,3)
# t2 = 1,2,3
# print(t1)
# print(t2)

# # tuple with one element
# t1 = (1)  # this is not a tuple, but an int
# print(type(t1))

# t2 = (1,) # this is a tuple with one element
# print(t2)

# x = 1
# y = 2


# x,y = 1,2
# print(x)
# print(y)

# user_input = tuple(input('Enter nubers: '))
# print(user_input)

# ----------------------------- Tuple Operations ----------------------------- #

# birth_date = (22, 3, 1990)
# # change tuple => imposible, but can convert it into list:
# l = list(birth_date)
# l[2] = 1991
# birth_date =  tuple(l)

# print(birth_date)

# compare tuples
t1 = (1,2,3)
t2 = (4,5)

print(cmp(t2,t1))
