class Cuboid:

    # Constructor
    def __init__(self, l, b, h: float) -> float:

        self.length = l
        self.breadth = b
        self.height = h

    # Method of class
    def lidArea(self: float) -> float:

        return self.length * self.breadth


# Object of class Cuboid
c1 = Cuboid(10, 5, 5)

print(c1.lidArea())
