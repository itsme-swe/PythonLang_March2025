class Arith:

    def sum(self, a, b, c=None):

        s = a + b

        if c == None:
            return s
        else:
            return s + c


a1 = Arith()

print(a1.sum(10, 20))  # 30

print(a1.sum(10, 20, 20))  # 50

"""
🔸 Here, we are acheiving polymorphism by method overloading. ' sum() ' function is performing calculation upon two parameters as well as for 3 parameters differently.

In python if we create one function with different parameters the last function over shadowed other functions automatically, but in C++ and java we can create one function with different parametrs.  

"""
