class Animal:
    def __init__(self):
        print('I am from Animal')

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('I am from Dog')

class Labrador(Dog):
    def __init__(self):
        print('I am from Labrador')
        super().__init__()

rocky = Labrador()

