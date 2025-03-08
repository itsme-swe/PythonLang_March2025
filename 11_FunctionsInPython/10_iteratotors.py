"""
🔸 An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets, etc.
"""

l1 = [2, 4, 6, 8, 10]

itr = iter(l1)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
