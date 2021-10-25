list_data = [[0] * 20 for i in range(20)]


for i in range(1,20):
    list_data[i][1:20] = list(map(int,input().split()))
# 6094번 문제 이해하고, 문제 다시 풀기 (map)

n = int(input())

for idx in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)

    for j in range(1,20):
        if list_data[j][y] == 0:
            list_data[j][y] = 1
        else:
            list_data[j][y] = 0

        if list_data[x][j] == 0:
            list_data[x][j] = 1
        else:
            list_data[x][j] = 0

for i in range(1, len(list_data[0])):
    for j in range(1, len(list_data[0])):
        print(list_data[i][j], end=' ')

    print()
