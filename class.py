class Door:
    def __init__(self, col, dim):
        self.color = col
        self.dimention = dim
    #class method
    def change_me(self, col, append_dim):
        self.color = col
        self.dimention.append(append_dim)
    def open(self):
        print('I am opening a ',
              self.color,
              ' colored door with dimentions',
              self.dimention)

red_door = Door('red', [1,2])
red_door.change_me('red', 5)
print(red_door)
