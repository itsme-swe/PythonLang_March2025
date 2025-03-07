list1 = [1, 3, 5, 7, 1, 9, 12, 14, 12, 10]

print("Before:", list1)  # Before: [1, 3, 5, 7, 1, 9, 12, 14, 12, 10]

print(len(list1))  # 10

list1.pop()

print("After:", list1)  # After: [1, 3, 5, 7, 1, 9, 12, 14, 12]

print(len(list1))  # 9

val = list1.pop(4)  # passed index as argument

print(val)  # 1 --- It returns the value from the specified index
