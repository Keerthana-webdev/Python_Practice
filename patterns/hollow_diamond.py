n = 5

# Upper part
for i in range(n):
    for j in range(2 * n - 1):

        if j == n - i - 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()

# Lower part
for i in range(n - 2, -1, -1):
    for j in range(2 * n - 1):

        if j == n - i - 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()