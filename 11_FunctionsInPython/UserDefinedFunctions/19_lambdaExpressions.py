# Here we are converting miles into kms
def miles2Km(miles):

    kms = 1.6 * miles

    return kms


print(miles2Km(10))  # 16.0

print()

# Now same we'll be performing with lambda expression

k = lambda miles: 1.6 * miles

print("Kms", k(10)) # Kms 16.0
