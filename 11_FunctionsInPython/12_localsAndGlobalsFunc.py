a = 10
b = 20
c = 30


def fun1(a=1, b=2):
    x = 5
    y = 7
    z = 9

    print(
        locals()
    )  # locals() function will call the local variable of function and it'll return dictionary


fun1()  # {'x': 5, 'y': 7, 'z': 9}

print(globals())
