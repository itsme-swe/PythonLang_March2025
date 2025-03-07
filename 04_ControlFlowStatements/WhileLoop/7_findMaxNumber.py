# Find max digit from number

n = 25562
max = float('-inf')

while n > 0:
  
  digit = n % 10
  if digit > max:
    max = digit

  n = n // 10

print(max)

