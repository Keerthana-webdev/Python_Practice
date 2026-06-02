n = 5

for i in range(n):
    for j in range(n):

        if i == 0 or \
           (j == n//2) or \
           (i == n-1 and j < n//2) or \
           (j == 0 and i > n//2 and i != n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()