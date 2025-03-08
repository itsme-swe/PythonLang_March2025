# Passing list as keyword argument


def addItem(item, l=[]):

    l.append(item)

    return l


L1 = [1, 2, 3, 4]

addItem(8, L1)  # function will pass 8 inside list L1

print(L1)  # [1, 2, 3, 4, 8]
