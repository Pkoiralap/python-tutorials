class Animal:
    def print(self):
        print('Print from Animal')

class Mammal(Animal):
    def print(self):
        print('Print from Mammal')

class Monkey(Animal,Mammal):
    def __init__(self):
        super().__init__()
        print('I am from Monkey')

mon = Monkey()
mon.print()

print(Monkey.__mro__)
# mro  --> method resolution order

