n = 4

for i in range(0, n):

    for j in range(0, n):

        if j < n - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

"""
* * * * 
* * *   
* *
*
"""
