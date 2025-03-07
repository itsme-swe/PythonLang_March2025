n = int(input("Enter the value of n: "))

while n > 0:
  r = n % 10
  n = n // 10
  print(r, end="")  # 5421