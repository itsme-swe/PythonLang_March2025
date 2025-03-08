# Positional Argument
def sum(a, b, c):

    print("Value of a:", a)
    print("Value of b:", b)
    print("Value of c:", c)

    r = a + b + c

    return r


total_Val = sum(5, 5, 5)

print(total_Val)  # 15

# Keyword Argument

total_Sum = sum(
    b=10, a=10, c=30
)  # In keyword argument we can pass actual parameters in any order, but we need to know the actual names of formal parameters

print(total_Sum)
