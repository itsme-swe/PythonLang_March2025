"""
🔸 isnumeric() method is a built-in method in Python that belongs to the string class. It is used to determine whether the string consists of numeric characters or not. It returns a Boolean value. If all characters in the string are numeric and it is not empty, it returns “True” If all characters in the string are numeric characters, otherwise returns “False”.

https://www.geeksforgeeks.org/python-string-methods/

"""

# Counting and Removing numeric characters

string = "123HelloWorld05061992"

count = 0

new_Str = ""

for ch in string:
    if ch.isnumeric():
        count += 1
    else:
        new_Str += ch

print("Number of numeric characters", count)  # Number of numeric characters 11

print(
    "Number of non-numeric characters", new_Str
)  # Number of non-numeric characters HelloWorld
