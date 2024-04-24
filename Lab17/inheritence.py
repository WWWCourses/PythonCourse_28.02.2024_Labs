class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self):
        return f'name={self.name}, age:{self.age}'

    # setters
    def setName(self, new_name):
        # do some log
        self.name = new_name

    # getters
    def getAge(self):
        return self.name

    def greet(self):
        print(f"Hello, I'm {self.name}, {self.age} years old!")


# Student IS A Person
class Student(Person):
    def __init__(self, name, age) -> None:
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.courses = []

    def enroll_class(self, course_name):
        self.courses.append(course_name)

    def greet(self):
        # Person.greet(self)
        super().greet()
        print('And I\'m a student!')

class Teacher:
    pass


pesho = Student('Pesho', 23)
pesho.enroll_class('Python')
pesho.greet()
