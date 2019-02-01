from math import pi

class Rect:
    def __init__(self, color, lenght, breadh):
        self.color, self.lenght, self.breadh = color, lenght, breadh
    def calc_area(self):
        self.area = self.lenght * self.breadh

class Circle:
    def __init__(self, color, radius, center):
        self.color, self.radius, self.center = color, radius, center
    def calc_area(self):
        self.area = 2 * pi * self.radius

r = Rect('red', 2, 5)
r.calc_area()

c = Circle('green', 5, (0,0))
c.calc_area()

def print_me(obj):
    print('type of object is', type(obj),' color is ',obj.color, ' area is ', obj.area)


print_me(r)
print_me(c)