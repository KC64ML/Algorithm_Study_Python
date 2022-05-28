t = int(input())
answer = ''
for i in range(t):
    a, b, c, d = map(int, input().split())
    result = max(0, min(b,d) - max(a, c))

    answer += f'#{i+1} {result}\n'

print(answer)