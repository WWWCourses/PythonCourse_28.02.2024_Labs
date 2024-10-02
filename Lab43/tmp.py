class A:
    def __init__(self):
        self.age = 34
        print('Constructor called!')
        self.greet('Pesho')

    def greet(self, name):
        print(f'Hello {name}')



a = A()
a.greet('Ada')
