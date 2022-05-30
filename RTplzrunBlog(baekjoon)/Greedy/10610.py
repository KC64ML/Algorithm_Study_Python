import sys

read = sys.stdin.readline

n = list(read().strip())

# 0이 없다면
if not n.count('0'):
    print(-1)
else:
    n = list(map(int, n))
    # 합이 3의 배수가 아니면 -1
    if sum(n) % 3:
        print(-1)
    else:
        n.sort(reverse=True)
        print(''.join(map(str, n)))



