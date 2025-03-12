# Creating Instance variable


class Test:

    # Constructor
    def __init__(self):

        self.instance_Variable1 = 10

    # Instance Method
    def fun(self):

        self.instance_Variable2 = 20


t1 = Test()

t1.fun()

t1.instance_Variable3 = 30  # instance variable

print(dir(t1))

"""
🔸 We can create instance variable inside constructor, inside instance method and outside the class also.
"""
