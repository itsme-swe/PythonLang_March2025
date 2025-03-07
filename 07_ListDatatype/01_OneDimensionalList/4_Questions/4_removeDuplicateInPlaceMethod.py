# Remove duplicate from list without using extra space

l1 = [3, 5, 9, 8, 3, 4, 5, 9, 6, 3, 7, 2]

l1.sort()

uniqEl = 1

for i in range(1, len(l1)):

    if l1[i] != l1[i - 1]:

        l1[uniqEl] = l1[i]

        uniqEl += 1

del l1[uniqEl:]

print(l1)  # [2, 3, 4, 5, 6, 7, 8, 9]
