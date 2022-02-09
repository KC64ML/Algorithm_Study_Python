from sys import stdin as s

n = int(s.readline())

arr = []

for _ in range(n):
    arr.append(s.readline().rstrip())

result = 0
result_data = arr[0]

for in_data in arr:
    if result < arr.count(in_data) and int(result_data) > int(in_data):
        result = arr.count(in_data)
        result_data = in_data


print(result_data)



