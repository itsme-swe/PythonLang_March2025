list1 = [2, 4, 6, 8, 10]

try:
    idx = int(input("Enter the index value: "))

    print(list1[idx])

except:
    print("Invalid Index value")

print("Terminated Gracefully")
