s1 = {"H", "A", "R"}

t = ("S", "H")

l = ["M", "E", "H"]

s1.add(t)

print(s1)  # {'A', ('S', 'H'), 'R', 'H'}

s1.update(l)

print(s1) # {'H', 'M', 'A', ('S', 'H'), 'R', 'E'}
