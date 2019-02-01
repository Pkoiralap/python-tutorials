class Cartesian:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0].x
            self.y = args[0].y
            self.z = args[0].z
        else:
            self.x, self.y, self.z = args
    def __add__(self, other):
        return Cartesian(self.x + other.x,
                         self.y + other.y,
                         self.z + other.z)

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'

point1 = Cartesian(5,6,7)
point2 = Cartesian(point1)
point3 = Cartesian(1,2,3)

print(point1)
print(point2)
print(point3)
summed_point = point1 + point2
summed_point += point3
print(summed_point)
