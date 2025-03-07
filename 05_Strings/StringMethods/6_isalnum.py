"""
🔸 isalnum() method is a string function in Python that checks if all characters in the given string are alphanumeric. If every character is either a letter or a number, isalnum() returns True. Otherwise, it returns False.

🔸 isalpha() method checks if all characters in a given string are alphabetic. It returns True if every character in the string is a letter and False if the string contains any numbers, spaces, or special characters.

"""

s = "Python123"

s1 = "Python!05"

print(s.isalnum())  # True

print(s1.isalnum())  # False

str1 = "Python 05"

str2 = "Volvo"

print(str1.isalpha())  # False
print(str2.isalpha())  # True
