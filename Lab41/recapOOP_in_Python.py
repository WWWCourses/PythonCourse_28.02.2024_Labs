class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        print('Init is called!')

    def greet(self):
        print(f'Hello,I am {self.name} ')

# instantiate Student objects
ivan = Student('Ivan',23)
pesho = Student(name='Pesho', age=19)

ivan.greet()
pesho.greet()
# Student.greet(self=ivan)




class QApplication:
    def __init__(self, args) -> None:
        pass

app = QApplication(3)


class QWidget:
    def __init__(self):
        self.width = 240
        self.height = 300
        self.windowTitle=''
        print('Init is called!')

    def setWindowTitle(self, title):
        self.title=title


window = QWidget()
window.setWindowTitle('Hello World')


