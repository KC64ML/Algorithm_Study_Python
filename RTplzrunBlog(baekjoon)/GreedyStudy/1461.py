import sys

read = sys.stdin.readline

n, m = map(int, read().split())

books = list(map(int, read().split()))

minus_arr = [0]
plus_arr = [0]
answer = 0

# 음수, 양수 부분 나누기
for book_loc in books:
    if book_loc < 0:
        minus_arr.append(book_loc * -1)
    else:
        plus_arr.append(book_loc)

minus_arr.sort(reverse=True)
plus_arr.sort(reverse=True)

for i in range(0, len(minus_arr), m):
    answer += (minus_arr[i] * 2)

for i in range(0, len(plus_arr), m):
    answer += (plus_arr[i] * 2)

answer -= max(max(minus_arr), max(plus_arr))

print(answer)
