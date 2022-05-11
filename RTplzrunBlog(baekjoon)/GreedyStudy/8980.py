import sys

read = sys.stdin.readline

n, c = map(int, read().split())
m = int(read())

box = []
result = [c] * (n + 1)
answer = 0

for i in range(m):
    a, b, c = map(int, read().split())
    box.append([a, b, c])

# (1)
# 도착 지점을 기준으로 정렬한다.
# 같다면, 출발 지점을 기준으로 정렬한다.

box.sort(key=lambda x: (x[1], x[0]))

# (2)
# 시작지점 ~ (도착지점 - 1) 까지 중 제일 작게 남은 잔여량을 찾는다.
# min(실은 용량, 잔여용량) 결과를 실은 박스 수에서 빼준다.

for i in range(m):
    left_idx = box[i][0]
    right_idx = box[i][1]
    capacity = min(result[left_idx:right_idx])
    cur_r = min(capacity, box[i][2])

    if not cur_r:
        continue
    else:
        answer += cur_r
        for j in range(left_idx, right_idx):
            result[j] -= cur_r

print(answer)
