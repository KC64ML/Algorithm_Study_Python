n = int(input())

max_row_size = 2 * n - 1
cnt = 0

# 1 ~ N - 1까지는 * 찍고, 빈칸 채우고, *찍기
# N부터 2 * N - 1까지는 반대로 돌리기

for idx in range(1, n):
    print("*"*idx+" " * 2*(n-idx) + "*"*idx)

for idx in range(n, 0, -1):
    print("*"*idx + " "*2*(n-idx) + "*"*idx)



