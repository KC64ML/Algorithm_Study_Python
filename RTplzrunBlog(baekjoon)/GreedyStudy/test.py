n, l = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(n)]
pool.sort()
cnt = 0

print(pool)

for i in range(n):
    st, ed = pool[i]
    if (ed - st) % l != 0:
        length = (ed - st) // l + 1  ## 웅덩이를 다 덮지 못하는 경우 1개를 추가한다.
    else:
        length = (ed - st) // l  ## 웅덩이가 딱 맞는 경우

    cnt += length
    new_ed = st + l * length
    print(length, cnt, new_ed)
    if (i + 1) < n:
        next_st = pool[i + 1][0]
        if new_ed > next_st:  ## 널빤지가 웅덩이를 초과해서 다음 웅덩이까지 덮는 경우
            pool[i + 1][0] = new_ed
print(cnt)
