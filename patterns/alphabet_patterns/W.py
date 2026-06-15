n = 5

for i in range(n):
    for j in range(2 * n - 1):

        if j == 0 or j == 2 * n - 2 or \
           (i + j == n - 1 and i >= n//2) or \
           (j - i == n - 1 and i >= n//2):
            print("*", end="")
        else:
            print(" ", end="")

    print()