import sys
import heapq


read = sys.stdin.readline

n = int(read())

arr = []

for _ in range(n):
    deadline, cupNoodle = map(int, read().split())
    arr.append((deadline, cupNoodle))

# 오름차순 정렬
arr.sort()

q = []
for in_arr in arr:
    heapq.heappush(q, in_arr[1])

    # heapq에 컵라면수가 저장된다.
    # 컵라면이 추가될 때마다 인덱스가 추가되는데 이는 단위시간 1씩 올라가는 것을 의미한다.
    # 컵라면이 추가되면 heapq 인덱스가 1씩 추가되는데, 만약 현재 마감시간이 heapq 길이보다 작다면,
    # heapq에 있는 컵라면 중 가장 작은 갯수를 가진 컵라면을 꺼낸다. (가장 작은 수 컵라면이 나온다.)
    # (이미 정렬이 된 상태에서 검사를 하기 때문에, 데드라인(마감시간)보다 heapq 길이가 크다면 heapq 데이터를 꺼낸다.)

    if in_arr[0] < len(q):
        t = heapq.heappop(q)


print(sum(q))