# import sys
#
# read = sys.stdin.readline
#
# n = int(read())
# arr = list(map(int, read().split()))
#
# arr.sort()
#
# result = 0
# arr_sum = 0
#
# for cur_data in arr:
#     arr_sum += cur_data
#     result += arr_sum
# print(result)



num = int(input())

data = list(map(int, input().split()))
data.sort()
result = 0

# 첫 번째수는 n 번, 두 번째수는 n - 1번, 세 번째수는 n - 2번 ~ 이렇게 된다.

for i in range(num):
    result += data[i] * (num - i)
print(result)
