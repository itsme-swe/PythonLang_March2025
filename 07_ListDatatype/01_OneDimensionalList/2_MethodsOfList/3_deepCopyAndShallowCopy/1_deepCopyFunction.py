import copy

list1 = [[2, 4, 6], [1, 3, 5]]

list2 = copy.deepcopy(list1)

list2[0][1] = 8

print("Copy of original:", list2)  # [[2, 8, 6], [1, 3, 5]]

print("original list:", list1)  # original list: [[2, 4, 6], [1, 3, 5]]

"""
🔸 deepcopy() creates new list with the copied items of original list, the changes made inside copied list won't affect original list. 
"""
