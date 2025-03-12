class Rectangle:

    def __init__(self, len, bre):

        self.__length = len
        self.__breadth = bre

    def get_length(self):

        return self.__length

    def set_length(self, length):

        self.__length = length

    def get_breadth(self):

        return self.__breadth

    def set_breadth(self, breadth):

        self.__breadth = breadth

    def area(self):

        return self.get_length() * self.get_breadth()


r1 = Rectangle(10, 10)

print(r1.area())  # 100

r1.set_length(20)
r1.set_breadth(10)

print(r1.area())  # 200
