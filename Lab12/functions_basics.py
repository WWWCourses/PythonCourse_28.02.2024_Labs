# ---------------------------- Function definition --------------------------- #
# def greet(user_name):
#     # user_name='Ada'
#     print('*'*50)
#     print(f'Hello, {user_name}')
#     print('*'*50)

# greet('Ada')
# greet('Maria')

# def add(x,y):
#     # x = 1
#     # y = 2
#     print(x+y)


# add( 1,2 )


# Example: List as argument
# def sum_list(x):
#     print( sum(x) )

# l = [1,2,3]
# sum_list( l ) # 6

# def print_last(l):
#     # l=[1,2]
#     print( l[-1] )

# print_last( [1,2] )

# Example: Dict as argument:
# def print_data(d):
#     print(f'name: {d["name"]}, age: {d["age"]}')

# data = {
#     'name': 'Ada',
#     'age':23
# }

# print_data(data) # 'name: Ada, age:23'



# ----------------------------- Default Parametrs ---------------------------- #
# def foo(x=100):
#     print(x)

# foo(1)
# foo()

# def greet_user(age, name='Anonymous'):
#     print(f'Hello, {name}. You are {age} years old')

# greet_user(23, 'Ada')
# greet_user(34)

# def bar(x, y=1, z=1):
#     print(x,y,z)

# bar(1,2,3)    # 1,2,3
# bar(1,2)      # 1,2,1
# bar(1)        # 1,1,1

# def print_name(first, last, middle=""):
#     print(f'{first} {middle} {last}')

# print_name('Ada', 'Byron')
# print_name('Maria', 'Ivanova', 'Popova')

# ----------------------------- Keyword Argument ----------------------------- #
# def print_user_data(name, age, town, height):
#     print(name, age, town, height)

# print_user_data('Ada', 23, 'sofia', 134)
# print_user_data(
#     age=23,
#     height=134,
#     name='Ada',
#     town='sofia'
# )


# def foo(x,y,z=1):
#     # x=2; y=1; z=1
#     print(x,y,z)

# # positional aguments
# # foo(1,2,3)

# # keyword arguments
# foo(y=1, x=2)


# def foo(x, y=1, z=2):
#     print(x,y,z)

# foo(1, z=99, y=4)   #1, 4 99


# def foo(a,b,c,d):
#     # a=1; b=2; error
#     print(a,b,c,d)

# foo( 1, 2, a=1, b=2) # error
# foo( 1, 2, c=1, d=2)


# ----------------------------------- *args ---------------------------------- #
# def add(*args):
#     print(args)
#     print(f'sum={sum(args)}')

# add(2)
# add(2,3)
# add(1,2,3)
# add(1,2,3,4)


# def foo(x, y, *args):
#     #x=1; y=2, args=(3,4,5)
#     print(x,y,args)

# foo(1,2,3,4,5)

# --------------------------------- **kwargs --------------------------------- #
# def foo(**kw):
#     print(kw)

# foo()
# foo(x=1)
# foo(x=1, y=2)


# def sum_values(**kw):
#     print( sum(kw.values()) )

# sum_values(x=1, y=2)        # 3
# sum_values(x=1, y=2, z=3)   # 6


# ------------------------------- Return Value ------------------------------- #
# def add(x,y):
#     print( f'sum={x+y}' )
#     return x+y

# res = add(1,2) ** 2;
# print(res)  # 9


# def foo():
#     print('Start')
#     return 5
#     print('END')

# res = foo() + foo()
# print(res)


# def foo():
#     print('Foo')

# res = foo()
# print(res)


# def foo(x):
#     res = x**2
#     print(f'res = {res}')
#     return res

# print( foo(2) + 3 )

# # res=4
# # 7


# def user_status(age):
#     # if age>=18:
#     #     return 'adult'
#     # else:
#     #     return 'child'

#     return 'adault' if age>=18 else 'child'



# print( user_status(21) ) # adult
# print( user_status(14) ) # child


# ----------------------------------- Scope ---------------------------------- #
def foo():
    x = 3
    print(x)

def bar():
    x = 6
    print(x)

x = 1
foo()
bar()
print( x)

