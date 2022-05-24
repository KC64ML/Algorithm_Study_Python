import sys

read = sys.stdin.readline

s = read().rstrip()
p = read().rstrip()

answer = 0

idx = 0

while idx < len(p):
    copy = ''

    # P의 마지막 구간을 S에서 찾았다면 끝내기
    if s.find(p[idx:]) != -1:
        answer += 1
        break

    for j in range(idx, len(p)):
        # 현재 인덱스에서 문자를 더해준다.
        copy += p[j]

        # 만약 더해진 문자가 s안에 없다면, 다음 번에 찾아야할 문자이다.
        if s.find(copy) == -1:
            answer += 1
            idx = j
            break

print(answer)
