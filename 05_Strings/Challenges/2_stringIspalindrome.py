"""
🔸 Checking string is palindrome. 

Palindrome is original string and reverse of string should be same

"""

str1 = "madam"

str2 = str1[::-1] # using slicing method to reverse the original string

if str1 == str2:
    print("Palindrome")
else:
    print("Not Palindrome")
