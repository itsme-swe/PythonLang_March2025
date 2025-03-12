class Rectangle:

    count = 0  # static / calss variable

    def __init__(self, l, b):

        self.length = l
        self.breadth = b

        Rectangle.count += 1  # To access the static variable we need to write "Class_Name.static_Variable"

    def perimeter(self):

        return 2 * (self.length + self.breadth)

    def area(self):

        return self.length * self.breadth

    @classmethod
    def countRectangle(Rectangle):

        print(Rectangle.count)


r1 = Rectangle(10, 5)
r2 = Rectangle(20, 15)
r3 = Rectangle(30, 5)

print(Rectangle.count)  # 3 ... Here we are calling class method 
