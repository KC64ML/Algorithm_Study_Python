from sys import stdin as s

a, b = map(int, s.readline().split())
m = int(s.readline())

arr = list(map(int, s.readline().split()))

arr = [0] + arr
b_result = []
a_result = arr[m]

for idx in range(1, m):
    a_result += pow(a, m - idx) * arr[idx]

while a_result:
    b_result.append(a_result % b)

    a_result //= b


for result in reversed(b_result):
    print(result, end=" ")

