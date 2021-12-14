# 안테나
# 정렬 후, 가운데 있는 것을 기준으로 한다.
# 정렬한 후, 가운데에서 가장 가까운 것을 기준

n = int(input())

list_data = list(map(int, input().split()))

sorted(list_data)

mid_data = (list_data[0] + list_data[len(list_data)-1])//2

result = 9999999999
result_idx = 0
for i in range(len(list_data)):
    check_data = abs(mid_data-list_data[i])

    if result > check_data:
        result = check_data
        result_idx = i



print(list_data[result_idx])
