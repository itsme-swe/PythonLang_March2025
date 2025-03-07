list1 = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

count = 0

for i in range(len(list1)):

    if list1[i] == 2:
        count += 1

print(count)  # 4

'''
🔸 Here we are counting the occurence of element 2.
'''