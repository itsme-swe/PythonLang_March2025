class NegativeAgeException(Exception):
    pass


def stage(age: int) -> int:

    if age < 0:
        raise NegativeAgeException("Age should not be negative")

    elif age >= 0 and age < 13:
        print("Kid")

    elif age >= 13 and age < 18:
        print("Teen")

    elif age >= 18 and age < 50:
        print("Young")

    else:
        print("Old")


age = int(input("Enter your age: "))

try:
    stage(age)  # calling stage function and passing age as argument
except NegativeAgeException as e:
    print(e)
