list1 = [1, 2, 3]

list2 = [4, 5, 6]

list1.extend(list2)

print(list1)  # [1, 2, 3, 4, 5, 6]


list1[len(list1) :] = list2  # slicing method

print(list1)  # [1, 2, 3, 4, 5, 6, 4, 5, 6]

a = [2, 4, 6]

b = [12, 14, 16]

a[:0] = b

print(a)  # [12, 14, 16, 2, 4, 6]
