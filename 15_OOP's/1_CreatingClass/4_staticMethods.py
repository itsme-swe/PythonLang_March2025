class Rectangle:
    # Class variable
    count = 0

    def __init__(self, l, b):

        self.length = l
        self.breadth = b

        Rectangle.count += 1  # To access the class variable we need to write "Class_Name.static_Variable"

    def perimeter(self):

        return 2 * (self.length + self.breadth)

    def area(self):

        return self.length * self.breadth

    @classmethod
    def countRectangle(Rectangle):

        print(Rectangle.count)

    @staticmethod
    def isSquare(len, bre):

        return len == bre


r1 = Rectangle(10, 10)

print(Rectangle.isSquare(10, 5))  # False 
