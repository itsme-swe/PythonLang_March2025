# Swapping elements of list using two pointer approach

arr = [2, 4, 6, 8]

i = 0
j = len(arr) - 1

while i < j:

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    i += 1
    j -= 1

print(arr)  # [8, 6, 4, 2]
