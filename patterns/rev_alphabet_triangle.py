n = 5

for i in range(n, 0, -1):
    ch = 65

    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1

    print()