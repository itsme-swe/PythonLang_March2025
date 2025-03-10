global_a = "I am global"


def outer():

    b = "I am enclosing"

    def inner():

        global global_a
        nonlocal b

        global_a = "Modifing global variable"
        b = "Modifing enclosing"

    inner()
    print("Inside outer function", b)


outer()

print("Outside outer", global_a)
