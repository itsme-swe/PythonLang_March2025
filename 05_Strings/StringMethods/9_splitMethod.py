"""
🔸  split() method splits a string into a list of strings after breaking the given string by the specified separator.

"""

myDate = input("Enter the date in dd/mm/yyyy format: ")

newDate = myDate.split("/")

print("Day: ", newDate[0])
print("Month", newDate[1])
print("Year", newDate[2])

"""
Enter the date in dd/mm/yyyy format: 05/06/2025
Day:  05 
Month 06 
Year 2025
"""
