def days():
    l1 = ["sun", "mon", "tues", "wed", "thrus", "fri", "sat"]

    i = 0

    while True:
        x = l1[i]
        i = (i + 1) % 7
        yield x


d = days()

print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
