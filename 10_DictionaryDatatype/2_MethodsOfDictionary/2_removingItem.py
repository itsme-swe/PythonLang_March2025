s1 = {101: "Rohan", 102: "Sohan", 103: {"Tison"}, 104: {"James"}}

del s1[104]  # remove particular key:value pair from dictionary

print(s1)  # {101: 'Rohan', 102: 'Sohan', 103: {'Tison'}}

print()

s2 = {"A": "Volvo", "B": "BMW", "C": "Honda", "D": "Tata"}

print(s2.pop("E", None))  # return None bcoz key is not present

print(s2.pop("D"))  # Function return the value of the key which has been removed

print(len(s2))  # 3

s2.clear()  # function removes all elements from list

print(len(s2))  # 0
