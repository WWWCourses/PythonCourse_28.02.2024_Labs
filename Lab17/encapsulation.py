class A:
    def __init__(self, id) -> None:
        self.__id = id


a = A(1)
a.__id = 2
print(a.__id)