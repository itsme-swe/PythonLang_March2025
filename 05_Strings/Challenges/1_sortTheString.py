# In this example we are sorting string and then joining them

str1 = "efacdgijlnm"

ss = sorted(str1)

print(ss)  # ['a', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'l', 'm', 'n']

ss1 = "".join(ss)

print(ss1)  # acdefgijlmn
