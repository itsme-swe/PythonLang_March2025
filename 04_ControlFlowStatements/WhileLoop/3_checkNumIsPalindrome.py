n = 121

temp = n
rev = 0

while n > 0:
  r = n % 10
  rev = rev * 10 + r
  n = n //10

if rev == temp:
    print("Num is palindrome")
else:
    print("Not palindrome")

# Num is palindrome