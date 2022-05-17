import sys

read = sys.stdin.readline

n, k = map(int, read().split())
number = list(read().rstrip())

stack = []
k_idx = k

for in_num in number:
    # k가 0보다 크고
    # stack의 마지막 값이 현재 입력된 숫자보다 작을 경우
    # pop
    # 1 4 로 입력 될 때는 stack = [1] -> [4]
    # 4 1 로 입력 될 때는 stack = [4, 1]
    # 현재 값보다 작은 값들은 모두 제외 시킨다.
    while k_idx > 0 and stack and stack[-1] < in_num:
        stack.pop()
        k_idx -= 1

    stack.append(in_num)

# 0 ~ n-k-1 까지 숫자가 가장 큰 수이다.
print(''.join(stack[:n-k]))
