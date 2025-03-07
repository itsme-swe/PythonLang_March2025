# Here we are using argument index with placeholders " {} " to print the string

a = 22

b = 7

c = a / b

print(
    "The division of {0} and {1} is {2}".format(a, b, c)
)  # The division of 22 and 7 is 3.142857142857143

print(
    "The division of {0} and {1} is {2:1.4}".format(a, b, c)
)  # The division of 22 and 7 is 3.143


print(f"The division of {a} and {b} is {c:1.3f}") # The division of 22 and 7 is 3.143
