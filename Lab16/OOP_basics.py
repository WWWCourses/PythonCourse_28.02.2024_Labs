
# class A:
#     # class attributes:
#     x = 2

#     # "constructor"
#     def __init__(self, name) -> None:
#         # set instance attributes
#         self.name = name

#     def __str__(self):
#         return f"name:{self.name}"

#     # instance method
#     def foo(self):
#         print('Foo')



# a1 = A('a1')
# a2 = A('a2')

# # access instance methods
# a1.foo()

# # access class attributes:
# print(A.x)
# print(a1.x)
# print(a2.x)

# # change class attribute:
# A.x = 100

# print(a1)
# print(a2)

# --------------------------- Operator overloading --------------------------- #
# class Account:
#     def __init__(self, owner, balance) -> None:
#         self.owner = owner
#         self.balance = balance

#     def __str__(self) -> str:
#         return f'owner: {self.owner}, balance: {self.balance}'

#     def __gt__(self, other):
#         return self.balance>other.balance

#     def __add__(self, other)->float:
#         return self.balance + other.balance



# a1 = Account('Maria', 1000)
# a2 = Account('Pesho', 1200)

# # Account.__add__(a1, a2)
# print(a1+a2) # 2200
# # Account.__gt__(a1, a2)
# if a1>a2:
#     print('A1 is bigger')


# ---------------------- Inspecting objects and classes ---------------------- #
# class A:
#     x = 1
#     def __init__(self, y) -> None:
#         self.y = y


# # print( a1.__init__(a1,9))
# a1 = A(9)


# print( a1.__dict__ )
# print( dir(a1) )



# ------------------------- Call a method from method ------------------------ #
# class A:
#     def __init__(self, id) -> None:
#         self.id = id

#     def method_1(self):
#         print('method_1 is called')
#         # call method2:
#         self.method_2()


#     def method_2(self):
#         print('method_2 is called')


# a = A(1)
# a.method_1()

# call method2
# a.method_2()



