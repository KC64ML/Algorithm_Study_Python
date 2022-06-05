import sys

read = sys.stdin.readline
t = int(read())

for i in range(t):
    n = int(read())
    arr = list(map(int, read().split()))
    answer = 0
    afterMAXDATA = arr[-1]
    for j in range(len(arr)-1, -1, -1):
        if afterMAXDATA < arr[j]:
            afterMAXDATA = arr[j]
        else:
            answer += (afterMAXDATA - arr[j])
    print(answer)
