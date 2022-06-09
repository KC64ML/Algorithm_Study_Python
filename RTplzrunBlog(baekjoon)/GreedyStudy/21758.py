n = int(input())
answer = 0
arr = list(map(int, input().split()))
s = []
s.append(arr[0])

for i in range(1, n):
    s.append(s[i - 1] + arr[i])

for i in range(1, n - 1):
    answer = max(answer, 2 * s[-1] - arr[0] - arr[i] - s[i])

for i in range(1, n - 1):
    answer = max(answer, s[-1] - arr[-1] - arr[i] + s[i - 1])

for i in range(1, n - 1):
    answer = max(answer, s[-1] + arr[i] - arr[0] - arr[-1])

print(answer)
