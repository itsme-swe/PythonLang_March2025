# Using _ for unused values

a, _, c = ("Harsh", 69.5, 32)

print(a)
print(c)

# Using * for variable length

a, *b = ("Harsh", 69.5, 32, True)

print(a)  # "Harsh"

print(b)  # [69.5, 32, True]

print(type(b))  # <class 'list'>
