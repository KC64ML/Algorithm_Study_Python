t = int(input())

for i in range(t):
    n, d = map(int, input().split())
    l = 1
    answer = 0
    while l <= n:
        l = l + (2 * d + 1)
        answer += 1

    print("#{} {}".format(i+1, answer))
