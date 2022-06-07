import sys
read = sys.stdin.readline

n = int(read())

arr = list(map(int, read().split()))

arr.sort()

answer = 0
in_a = 0
for in_arr in arr:
    in_a += in_arr
    answer += in_a

print(answer)