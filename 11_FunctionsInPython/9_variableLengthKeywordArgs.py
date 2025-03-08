# Variable length keyword arguments


def fun1(**kwargs):

    print(kwargs)
    print(type(kwargs))


fun1(name="Toyota", carName="Fortuner", engine=3.8)

"""
{'name': 'Toyota', 'carName': 'Fortuner', 'engine': 3.8}
<class 'dict'>

"""

print()


# Iterating over kwargs
def fun2(**kwargs):

    for i in kwargs:
        print(i, kwargs[i])


fun2(name="Harsh", age=32, weight=69.5)
"""
name Harsh    
age 32        
weight 69.5 

"""

print()


def fun3(**kwargs):

    for i, j in kwargs.items():
        print(i, j)


fun3(name="Mukul", age=32, weight=75.5)

"""
name Mukul
age 32
weight 75.5

"""
