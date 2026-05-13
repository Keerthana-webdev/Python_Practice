n = 5

for i in range(n):
    ch = 65

    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1

    print()