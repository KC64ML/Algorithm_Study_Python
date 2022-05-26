t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    visited = [[False] * (n+1) for _ in range(n+1)]
    check = False
    answer = 'yes'
    for _ in range(n):
        arr.append(list(map(str, input().rstrip())))

    for r in range(n):
        for c in range(n):
            if arr[r][c] == '#' and not visited[r][c] and not check:
                cnt = 0
                for k in range(c, n):
                    if arr[r][k] == '.':
                        break
                    else:
                        visited[r][k] = True
                        cnt += 1
                # print("r, c, cnt", r, c, cnt)
                for in_i in range(r+1, r+cnt):
                    for in_j in range(c, c+cnt):
                        # print(in_i, in_j)
                        visited[in_i][in_j] = True
                        if arr[in_i][in_j] == '.':
                            answer = 'no'
                            check = True
                            break
                    if check:
                        break
                check = True
            elif arr[r][c] == '#' and not visited[r][c] and check:
                answer = 'no'
                break

    print("#{} {}".format(i+1, answer))