array_list = [[0] * 11 for i in range(11)]

for n in range(1, 11):
    array_list[n][1:11] = list(map(int,input().split()))

i = 2; j = 2

while True:
    if array_list[i][j] == 2:
        array_list[i][j] = 9
        break

    if array_list[i][j+1] == 1:
        if array_list[i+1][j] == 1:
            array_list[i][j] = 9
            break
        else:
            array_list[i][j] = 9
            i += 1
    else:
        array_list[i][j] = 9
        j += 1

for row in range(1,11):
    for col in range(1,11):
        print(array_list[row][col], end =' ')
    print()