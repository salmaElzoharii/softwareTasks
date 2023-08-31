n = int(input())
while(n>8 or n<1):
 n = int(input())

counter = 0

nOfspace = n - 1

for i in range(1, n + 1):
    for j in range(nOfspace):
        print(" ", end="")

    while i:
        if counter == i:
            break
        print("#", end="")
        counter += 1

    print("  ", end="")

    while counter:
        print("#", end="")
        counter -= 1

    print()
    nOfspace -= 1

