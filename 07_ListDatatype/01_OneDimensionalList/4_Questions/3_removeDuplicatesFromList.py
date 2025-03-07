# Remove the duplicates from the list

l1 = [3, 5, 9, 8, 3, 4, 5, 9, 6, 3, 7, 2]

l2 = []

for i in range(len(l1)):

    if l1[i] not in l2:

        l2.append(l1[i])

print(l2)  # [3, 5, 9, 8, 4, 6, 7, 2]
