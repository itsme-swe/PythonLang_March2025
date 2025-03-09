# This is the mixture of Arguments


def add(a, b, /, c=0, *, e, f):

    result = a + b + c + e + f

    return result


sum_Val = add(10, 10, e=5, f=5)

print(sum_Val)

"""
🔸 Before / a and b is positional argument
🔸 After * e and f are keyword arguments 
"""
