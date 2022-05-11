import sys

read = sys.stdin.readline

n, l = map(int, read().split())

puddle = []

for _ in range(n):
    sta, arri = map(int, read().split())
    puddle.append([sta, arri])

puddle.sort()
answer = 0

for i in range(n):
    left, right = puddle[i]
    t = (right - left) % l
    if t:
        length = (right - left) // l + 1  # 웅덩이를 다 덮지 못하는 경우 1개를 추가한다.
    else:
        length = (right - left) // l  # 웅덩이가 딱 맞는 경우

    answer += length
    arrival = left + length * l
    # 마지막 위치가 아닐 때
    if (i + 1) < n:
        if arrival > puddle[i + 1][0]:
            puddle[i + 1][0] = arrival  # 널빤지가 웅엉이를 초과해서 다음 웅덩이 까지 덮는 경우

print(answer)
