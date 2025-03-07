import copy

list1 = [[2, 4, 6], [1, 3, 5]]

list2 = copy.copy(list1)

list2[1][2] = 11

print("Shallow Copy:", list2)  # Shallow Copy: [[2, 4, 6], [1, 3, 11]]

print("Original Copy:", list1)  # Original Copy: [[2, 4, 6], [1, 3, 11]]

"""
🔸 shallow copy made changes inside the original copy also.
"""
