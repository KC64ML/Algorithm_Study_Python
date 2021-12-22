

t = int(input())




while t > 0:
    n, m = map(int, input().split())
    list_array = (list(map(int, input().split())))
    list_array2 = []
    idx = 0
    for _ in range(n):
        list_array2.append(list_array[idx:idx+m])
        idx += m

    result = 0
    total_result = 0

    for i in range(n):

        print("시작 : idx", i)
        result = list_array2[i][0]
        print(list_array2[i][0], end = ' ')
        for j in range(1, m):
            # 오른쪽 위 : ru
            # 오른쪽 : r
            # 오른쪽 밑 : rd
            ru = 0
            r = 0
            rd = 0
            if not(i + 1 >= n or j >= m):
                rd = list_array2[i + 1][j]
                i += 1

            if not(i - 1 < 0 or j >= m):
                ru = list_array2[i - 1][j]
                i -= 1

            if not(j >= m):
                r = list_array2[i][j]

            result += max(rd, ru, r)

            print(max(rd, ru, r), end = ' ')
        total_result = max(total_result, result)
        print("result 결과 : ",result)
    print(total_result)
    t -= 1





