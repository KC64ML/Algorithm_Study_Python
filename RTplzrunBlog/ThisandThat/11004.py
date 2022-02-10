from sys import stdin as s

n, k = map(int, s.readline().split())

list_data = list(map(int, s.readline().split()))

list_data.sort()
print(list_data[k-1])
