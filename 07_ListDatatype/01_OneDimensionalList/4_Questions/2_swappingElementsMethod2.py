# Swapping elements of list using two pointer approach but this without taking extra temp variable

arr = [2, 4, 6, 8]

i = 0

j = len(arr) - 1

while i < j:

    arr[i], arr[j] = arr[j], arr[i]

    i += 1
    j -= 1

print(arr)  # [8, 6, 4, 2]
