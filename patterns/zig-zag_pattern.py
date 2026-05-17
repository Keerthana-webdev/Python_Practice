n = 9

for i in range(3):
    for j in range(n):

        if ((i + j) % 4 == 0) or (i == 1 and j % 4 == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()