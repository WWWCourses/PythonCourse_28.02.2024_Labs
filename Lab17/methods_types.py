class A():
    def __init__(self, id) -> None:
        # self = s1
        print('Constructor is called!')
        self.id = id
        # return self

    @classmethod
    def class_method(cls, id):
        # cls = A
        print('Class method is called!')
        return cls(2)

    @staticmethod
    def foo(x):
        print(f'Static method called with x = {x}')

    def instance_method(self, x):
        # self = s1
        print(x)


# create instances/objects:
s1 = A(1)
# call/invoke class method
s2 = A.class_method(1)

# call static method
s1.foo(1)

# call instance method
s1.instance_method(1)






