lt1 = [2, 4, 6, 8, 10]

for x in range(len(lt1)):

    print(lt1[x], end=" ")  # 2 4 6 8 10

print()

# Printing list in reverse order
for i in range(len(lt1) - 1, -1, -1):
    print(lt1[i], end=" ")

# 10 8 6 4 2

"""
This upper python code is similar to the java for loop:

for(int i = 0; i < lt1.length; i++) {
  System.out.print(lt1[i] + " ")
}

"""
