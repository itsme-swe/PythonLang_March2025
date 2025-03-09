# In this function we are specifying the return type of function explicitly by using '->'
def greet(name: str) -> str:

    return f"Hello, {name}"


guest1 = greet("Harsh")

print(guest1)

print()

# 🔸 Similarly, here function will return int value


def add(a, b: int) -> int:

    return a + b


sum = add(10, 20)

print(sum)  # 30
