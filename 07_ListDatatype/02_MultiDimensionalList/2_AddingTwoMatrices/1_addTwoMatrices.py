a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

sum = []

for i in range(len(a)):

    s = []

    for j in range(len(a[i])):

        s.append(a[i][j] + b[i][j])

    sum.append(s)

# Printing  list sum[][]

for i in range(len(sum)):

    for j in range(len(sum[i])):

        print(sum[i][j], end=" ")

    print()

"""
10 10 10 
10 10 10 
10 10 10 

"""
