l1 = [1, 2, 3, 4]

l2 = [5, 10, 15, 20]

# 🔸 Here we are using map() function on list l1 and multipying each value with 3
m = map(lambda x: x * 3, l1)

print(list(m))  # [3, 6, 9, 12]

print()

# 🔸 Now adding both the list using map function

m1 = list(map(lambda i, j: i + j, l1, l2))

print(m1)  # [6, 12, 18, 24]

print()

# 🔸 Using map() to convert a list of strings to uppercase.

s1 = ["apple", "orange", "mango"]

s = list(map(lambda x: x.upper(), s1))

l = list(map(str.capitalize, s1))  # making first letter to capital

print(s)  # ['APPLE', 'ORANGE', 'MANGO']

print(l)  # ['Apple', 'Orange', 'Mango']
