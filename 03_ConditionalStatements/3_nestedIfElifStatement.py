john = int(input("Enter the age of john: "))
smith = int(input("Enter the age of smith: "))
ajay = int(input("Enter the age of ajay: "))

if john > smith and john > ajay:
  print("John is greater")

elif smith > john and smith > ajay:
  print("Smith is greater")

else: 
  print("Ajay is greater")