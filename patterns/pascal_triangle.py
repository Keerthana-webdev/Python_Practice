n = 10

for i in range(n):
    num = 1
    print(" " * (n - i), end="")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()