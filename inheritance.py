class Person:
    def __init__(self, name, age):
        self.name, self.age = name ,age
    def print(self):
        print(self.name + '-' + str(self.age) + '-' + str(self.roll_no))

class Student(Person):
    def __init__(self, name, age, roll_no):
        Person.__init__(self, name, age)
        self.roll_no = roll_no

class Teacher(Person):
    def __init__(self, name, age, teacher_id=0):
        super().__init__(name, age)
        self.teacher_id = teacher_id
    def print(self):
        print(self.name + '-' + str(self.age) + '-' + str(self.teacher_id))

nished = Teacher('Nished', 48, 10192)
nished.print()