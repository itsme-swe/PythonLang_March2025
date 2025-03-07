# Print n terms of Fibonacci Series

n = int(input("Enter the value of n: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
