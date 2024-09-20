def great(user_name):
    print(user_name)

class A:
    def great(self, user_name):
        print(user_name)

class B(A):
    pass

# Call function
great('Ada')

# create instance of A
a1 = A()

# create instance of B
b1 = B()

# Call methods
a1.great('Ada Byron')
b1.great('Ada Byron')

