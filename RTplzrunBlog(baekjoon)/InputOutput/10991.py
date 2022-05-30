n = int(input())

for idx in range(1, n + 1):
    print(" " * (n - idx),end="")
    for in_idx in range(idx):
        print("*", end=" ")

    print()

