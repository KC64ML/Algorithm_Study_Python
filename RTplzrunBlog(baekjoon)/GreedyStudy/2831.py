import sys

read = sys.stdin.readline

n = int(read())

arr = list(map(int, read().split()))
arr2 = list(map(int, read().split()))


nman = []
pman = []

nwoman = []
pwoman = []

for in_arr in arr:
    if in_arr < 0:
        nman.append(in_arr)
    else:
        pman.append(in_arr)

for in_arr in arr2:
    if in_arr < 0:
        nwoman.append(in_arr)
    else:
        pwoman.append(in_arr)

answer = 0

nman.sort(reverse=True)
pman.sort()
nwoman.sort(reverse=True)
pwoman.sort()

def calForResult(plus, minus):
    j = 0
    cnt = 0
    for i in range(len(plus)):
        while j < len(minus):
            if plus[i] + minus[j] < 0:
                j += 1
                cnt += 1
                break
            else:
                j += 1
        if j == len(minus):
            break

    return cnt


answer += calForResult(pman, nwoman)
answer += calForResult(pwoman, nman)

print(answer)
