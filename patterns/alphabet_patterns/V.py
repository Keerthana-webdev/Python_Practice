n = 5

for i in range(n):
    for j in range(2 * n - 1):

        if j == i or j == 2 * n - 2 - i:
            print("*", end="")
        else:
            print(" ", end="")

    print()