import sys

read = sys.stdin.readline

n, m = map(int, read().split())
arr = list(map(int, read().split()))

arr = arr + [0] * (10001 - len(arr))


start = 0
end = 0
partition = 0

result = 0

# end <= n인 이유 (원래 마지막 인덱스가 n - 1이다.)
# end가 마지막 인덱스에 도착하고 다음으로 넘어갈 때, 더이상 갈곳이 없어
# start를 돌려줘야 한다.


while end <= n:
    # 현재 원하는 m보다 작을 경우, end를 증가
    # 햔제 원하는 m과 같거나 클 경우, start를 증가
    if partition < m:
        partition += arr[end]
        end += 1
    elif partition >= m:
        partition -= arr[start]
        start += 1

    print("start : ", start, " end : ", end, "result : ", result, end=" ")
    print("permission : ", partition, " arr[start] : ", arr[start], "arr[end] : ", arr[end])

    # 도착했다면 횟수를 증가한다.
    if partition == m:
        result += 1

print(result)