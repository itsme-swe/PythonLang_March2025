"""
🔸 Checking two strings are anagram 

Anagram is if alphabets of two strings are same than it is called as anagram

"""

s1 = "decimal"

s2 = "medical"

if len(s1) != len(s2):
    print("Not an Anagram")

else:

    for ele in s1:
        if ele not in s2:
            print("Not an Anagram")
            break

    else:
        print("Anagram")
