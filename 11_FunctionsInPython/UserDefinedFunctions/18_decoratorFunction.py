def decorator(fun):

    def wrapper():

        print("*" * 5)

        fun()

        print("*" * 5)

    return wrapper


@decorator
def display():
    print("Hello World")


display()

"""
*****
Hello World
***** 

"""
