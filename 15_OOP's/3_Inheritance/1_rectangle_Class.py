class Rectangle:

    def __init__(self, len, bre):

        self.length = len
        self.breadth = bre

    def area(self):
        return self.length * self.breadth

    def perimenter(self):

        return 2 * (self.length + self.breadth)


# Inheriting from parent class
class Cuboid(Rectangle):

    def __init__(self, len, bre, hei):

        self.height = hei

        super().__init__(len, bre)  # calling parent class constructer

    def volume(self):

        return self.length * self.breadth * self.height


c1 = Cuboid(5, 5, 5)

print(c1.volume())
