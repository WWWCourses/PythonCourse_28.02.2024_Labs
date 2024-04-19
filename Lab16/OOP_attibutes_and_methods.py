# ------------------------- Static Attribute Use Case ------------------------ #
# class A:
#     # static (class) attribute
#     count = 0

#     def __init__(self, id) -> None:
#         self.id = id
#         A.count += 1


# if __name__=="__main__":
#     a1 = A(1)
#     a2 = A(2)
#     a3 = A(3)

#     print(f'Objects created: {A.count}')


# ------------------------------- Class Method ------------------------------- #
# A class method receives the class as implicit first argument (just like an instance method receives the instance)

class A:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['name'])



a1 = A(id=1, name='a1')

a2_data = {'id': 2, 'name':'a2'}
a2 = A.from_dict(a2_data)

print(a2.id)
