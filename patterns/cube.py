n = 5

# Outer loop for layers
for i in range(1, n + 1):

    # Print i layers of size i x i
    for k in range(i):
        for j in range(i):
            print(1, end=" ")
        print()

    print()