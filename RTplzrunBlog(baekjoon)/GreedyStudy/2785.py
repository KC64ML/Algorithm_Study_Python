import sys

read = sys.stdin.readline

n = int(read())

chain = list(map(int, read().split()))

chain.sort()

s = 0
answer = 0
for i in range(len(chain)):
    # 남아있는 체인의 개수
    cnt = n - i - 1

    # 현재 만들 수 있는 체인의 길이를 더해준다.
    # 체인 길이 : 고리
    # 고리의 수를 늘려가며, 남아있는 체인을 묶어준다.
    s += chain[i]
    print(cnt, s)
    if s >= cnt:
        print(s)
        answer = cnt
        break

print(answer)
