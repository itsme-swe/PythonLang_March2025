total_Amount = 150000000000


def add(a, b: int) -> int:
    return a + b


def sub(x, y: int) -> int:
    return x - y


"""
🔸 The below code will only execute when we'll run this current file as program file but if we import this file in some another program the below code will not execute.
"""
if __name__ == "__main__":

    print(__name__)

    print(f"From module one {add(10,20)}")

    print(f"From module one {abs(sub(10,30))}")
