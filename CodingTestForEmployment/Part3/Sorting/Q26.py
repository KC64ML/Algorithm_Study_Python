# Q26 카드 정렬하기
from queue import PriorityQueue

n = int(input())

pq = PriorityQueue()

for _ in range(n):
    pq.put(int(input()))

result = pq.get()


for i in range(n-1):
    cur_data = pq.get()
    print("result : ", result, " hq[i] : ", cur_data)
    result = (result + cur_data)
    pq.put(result)

    print(result)


print(pq.qsize())

total = 0

for _ in range(pq.qsize()):
    total += pq.get()

print(total)
