class A:
    def __init__(self, id) -> None:
        self.id = id



objects = [
    A(1),
    A(2),
    A(3)
]

for idx, o in enumerate(objects, start=1):
    print(f'idx: {idx}, id: {o.id}')