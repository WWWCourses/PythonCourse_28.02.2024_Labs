class A:
    def __init__(self,x):
        self.x = x

    def foo(self):
        print(f'Foo in A: {self.x}')


a1 = A(1)
a2 = A(2)

print(a1.x)
print(a2.x)


a1.foo()
a2.foo()