import sys

read = sys.stdin.readline
n = int(read())

arr = []

for _ in range(n):
    arr.append(list(map(int, read().strip())))


def quad_tree(c_size, x, y):
    if c_size == 1:
        print(arr[x][y], end="")
        return

    check = False

    for i in range(x, x + c_size):
        for j in range(y, y + c_size):
            if arr[i][j] != arr[x][y]:
                check = True
                break
        if check:
            break

    if not check:
        print(arr[x][y], end="")
    else:
        c_size //= 2

        print("(", end="")
        quad_tree(c_size, x, y)
        quad_tree(c_size, x, y + c_size)
        quad_tree(c_size, x + c_size, y)
        quad_tree(c_size, x + c_size, y + c_size)
        print(")", end="")


quad_tree(n, 0, 0)

# 참고 : https://dojinkimm.github.io/problem_solving/2020/01/08/boj-1992_quadtree.html