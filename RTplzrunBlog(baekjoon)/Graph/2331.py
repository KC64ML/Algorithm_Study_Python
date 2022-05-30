from sys import stdin as s

a, p = map(int, s.readline().split())


cur_value = [a]

while True:
    cnt = 0

    for cur_data in str(cur_value[-1]):
        cnt += int(cur_data) ** p

    if cnt in cur_value:
        break

    cur_value.append(cnt)

print(cur_value.index(cnt))
