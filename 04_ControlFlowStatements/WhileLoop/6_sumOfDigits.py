# Find the sum of digits

n = 55555
sum = 0

while n > 0:
  r = n % 10
  sum += r
  n = n // 10

print(sum)