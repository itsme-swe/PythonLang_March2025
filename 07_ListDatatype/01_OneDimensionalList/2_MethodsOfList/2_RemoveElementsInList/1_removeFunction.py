list1 = [20, 30, 20, 50, 50, 30]

item = [20, 50]

print("List before removing element: ", list1)  # [20, 30, 20, 50, 50, 30]

list1.remove(20)  # remove first occurence of the given element

print("List after removal: ", list1)  # List after removal:  [30, 20, 50, 50, 30]

# Removing multiple elements 
for ele in item:
    if ele in list1:
        list1.remove(ele)

print(list1)  # [30, 50, 30]
