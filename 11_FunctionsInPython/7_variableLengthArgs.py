# Variable Arguments


def fun1(*args):

    print(type(args), args)


fun1()
fun1(10, 20)
fun1(10, 20, 30, 40, 50)
fun1("Hello", 20, 69.5)
