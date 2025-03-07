list1 = [25, 10, 55, 15, 10, 5]

max = float("-inf")

for i in range(len(list1)):
    if list1[i] > max:
        max = list1[i]

print(f"The maximum element in list is {max}")
