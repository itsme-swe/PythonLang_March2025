file1 = open("contact.txt", "r")  # opening the file

str1 = file1.read()  # then reading the file

print(str1)


file1.close() # always close the file's after using them
