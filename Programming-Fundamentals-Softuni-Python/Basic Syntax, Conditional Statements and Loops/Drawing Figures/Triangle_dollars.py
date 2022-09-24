number = int(input())

for i in range(1, number + 1):
    for j in range(0, i, +1 ):
        print("$", end=" ")
    print()