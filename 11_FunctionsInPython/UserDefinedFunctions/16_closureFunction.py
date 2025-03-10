# Python closure is similar to JS closure


# Normal Example
def closure(msg: str) -> str:

    def display():

        print(msg)

        print("*" * 5)

    return display


outer_Func = closure("Hello World")

outer_Func()

"""
Hello World
*****

"""

print()


# Example 2 for closure
def count() -> int:

    count = 0

    def increment():

        nonlocal count  # Without 'nonlocal', count will be read-only
        count += 1
        return count

    return increment


count_Instance = count()

print(count_Instance()) # 1
print(count_Instance()) # 2
