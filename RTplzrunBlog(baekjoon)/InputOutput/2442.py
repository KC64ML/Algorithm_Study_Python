n = int(input())

blank_len = 0
star_len = 0

for idx in range(1, n + 1):
    blank_len = (2 * n - 1) // 2 - (idx - 1)
    star_len = (2 * idx - 1)

    for b_idx in range(blank_len):
        print(" ",end="")
    for s_idx in range(star_len):
        print("*",end="")

    print()
