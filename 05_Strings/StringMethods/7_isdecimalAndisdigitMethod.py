"""
🔸 isdecimal() method is a quick and easy way to check if a string contains only decimal digits. It works by returning True when the string consists of digits from 0 to 9 and False otherwise.

🔸 isdigit() method is a built-in Python function that checks if all characters in a string are digits. This method returns True if each character in the string is a numeric digit (0-9), and False otherwise.

"""

a = "1234"

b = "12a345"

c = "51,000"

print(a.isdecimal())  # True
print(b.isdecimal())  # False
print(c.isdecimal())  # False

s1 = "0141"

s2 = ""

s3 = "-1234"

print(s1.isdigit())  # True
print(s2.isdigit())  # False
print(s3.isdigit())  # False
