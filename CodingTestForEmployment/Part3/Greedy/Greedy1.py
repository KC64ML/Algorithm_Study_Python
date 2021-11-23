n = int(input())
list_data = []

list_data = list(map(int,input().split()))

list_data.sort()
last_data = list_data[n-1]
total_cnt = 0

for idx in range(1,last_data+1):
    if list_data.count(idx) >= idx:
        total_cnt += 1

print(total_cnt)