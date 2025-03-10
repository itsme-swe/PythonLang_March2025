# Handling Zero Division Error


# Function to divide two values
def div(a, b: int) -> int:

    if b != 0:

        c = a // b
        return c

    else:
        raise ZeroDivisionError


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Main block bcoz we are calling function here
try:
    c = div(a, b)
    print(c)
except:
    print("ZeroDivisionError")
