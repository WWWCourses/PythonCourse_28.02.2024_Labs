# class A:
#     # class attribute
#     name='A object'


# # instatiating objects of class A
# a1 = A()
# a2 = A()

# a1.id = 1
# a2.id = 2


# show object attributes
# print(a1.__dict__)
# print(a2.__dict__)

# read class attributes
# print(a1.name)
# print(a2.name)
# print(A.name)


# ----------------------------- Instance Methods ----------------------------- #
# class A:
#    def instance_method(self):
#       # self = a1
#       print(self)


# a1 = A()
# a2 = A()

# print(a1)
# print(a2)
# a1.instance_method()
# a2.instance_method()

# Example 2
# class Person:
#   def greet(self):
#     print("Hi there! I'm", self.name)

# # create some objects of class Person:
# maria = Person()
# # maria.name= "Maria Popova"

# pesho = Person()
# # pesho.name = "Pesho"

# # call greet:
# maria.greet()
# pesho.greet()


# -------------------- "Constructor" == __init__() method -------------------- #
# class A:
#     def __init__(self, id):
#         print('A constructor is called!')
#         self.id = id


# a1 = A(1)
# a2 = A(2)

# print(a1.id)
# print(a2.id)


# # example 2
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hi there! I'm", self.name)



# # create some objects of class Person:
# maria = Person("Maria Popova")
# pesho = Person("Pesho")


# # call greet:
# maria.greet()
# pesho.greet()

