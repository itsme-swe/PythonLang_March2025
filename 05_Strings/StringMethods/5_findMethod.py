s = "Python is fun"

print(s.find("python"))  # Returns -1 bcoz Python is not present

print(s.find("Python"))  # Returns 0 bcoz P's first occurence is at 0th index value

print(s.rfind("n"))

print(s.index("thon"))  # Return index value of substring, 2 

'''
🔸 find()  returns the index of the first occurrence of a substring within a given string. If the substring is not found, it returns -1.
'''