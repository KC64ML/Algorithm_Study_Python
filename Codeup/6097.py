h, w = map(int, input().split())
n = int(input())

array_list = [[0] * (w+1) for i in range(h+1)]

while True:
    if n <= 0: break

    l, d, x, y = map(int, input().split())

    if d == 0:
        for n_in in range(y, y+l):
            array_list[x][n_in] = 1
    else :
        for n_in in range(x, x + l):
            array_list[n_in][y] = 1

    n -= 1


for i in range(1,h+1):
    for j in range(1,w+1):
        print(array_list[i][j], end = ' ')

    print()
