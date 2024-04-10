# -------------------------------- Scope Basic ------------------------------- #
# def foo():
#     x = 5
#     print(f'x in foo: {x}')

# def bar(x):
#     print(f'x in bar: {x}')

# x = 1
# foo()
# bar(9)
# print(f'x in global: {x}')


# global = {
#     foo: 0x1233,
#     bar: 0x1232,
#       x: 1,
# }


# # will be deleted after =foo() ends
# bar = {
#     x:5
# }

# # will be deleted after bar() ends
# bar = {
#     x:9
# }


###Example: change global variable in funciton
# Variant 1
# number = 1
# def increment(number):
#     # number+=1

#     number = number + 1
#     return number

# number = increment(number)
# print(number) # 2

# Variant 2: using gloabl keyword
# number = 1
# def increment():
#     global number
#     number+=1


# increment()
# print(number) # 2

# ---------------------- Pass values vs Pass References ---------------------- #
### Pass by value (for all imutable types)
# def foo(x):
#     # x = 1
#     x = 100
#     print(y) # 1
#     print(x) # 100

# y = 1
# foo(y)
# print(f'y in main: {y}')

# # global = {
# #     y :0x123
# # }

# # foo = {
# #     x:0x125
# # }

# ### Pass by reference (for all mutable types)
# def foo(x):
#     # x = y
#     x[0] = 100
#     print(y) #[100]
#     print(x) # [100]


# y = [1]
# foo(y)
# print(f'y in main: {y}')

# # global = {
# #     y :0x123
# # }

# # foo = {
# #     x:0x123
# # }
