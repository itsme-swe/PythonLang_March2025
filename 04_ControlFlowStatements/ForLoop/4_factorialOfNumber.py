# Factorial of given number

n = int(input("Enter the value of n: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("The factorial of ", n, "is: ", fact)

"""
Enter the value of n: 5
The factorial of  5 is:  120
"""
