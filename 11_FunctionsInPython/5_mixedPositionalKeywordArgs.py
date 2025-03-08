# For mixed positional argument we use '/' in between positional and keyword argument


def add(a, b, /, c=0, d=0):

    result = a + b + c + d

    return result


sum_Value = add(10, 10, d=5, c=5)  # 30

sum_Val = add(10, 10)  # 20

print(sum_Value)

print(sum_Val)
