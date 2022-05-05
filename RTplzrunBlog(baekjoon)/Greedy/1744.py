import sys

read = sys.stdin.readline

n = int(read())

arr = []

# 음수, 양수, 1 리스트 만들기
minus_list = []
plus_list = []
one_list = []
ans = 0

# 입력 값 받기
for i in range(n):
    input_num = int(input())
    if input_num > 1:
        plus_list.append(input_num)
    elif input_num  <= 0:
        minus_list.append(input_num)
    else:
        one_list.append(input_num)

plus_list.sort(reverse=True)
minus_list.sort()

# 양수 계산
# 양수의 개수가 홀수라면 제일 작은 값을 정답에 더하기
if len(plus_list) % 2 == 1:
    ans += plus_list[len(plus_list)-1]
    for j in range(0, len(plus_list)-1,2):
        ans += plus_list[j] * plus_list[j+1]
# 양수의 개수가 짝수면 두 수를 곱하고 정답에 더하기
else:
    for j in range(0, len(plus_list), 2):
        ans += plus_list[j] * plus_list[j+1]

# 음수 계산(0 포함)
# 음수의 개수가 홀수라면 제일 작은 값을 정답에 더하기
if len(minus_list) % 2 == 1:
    ans += minus_list[len(minus_list)-1]
    for j in range(0, len(minus_list)-1, 2):
        ans += (minus_list[j]) * (minus_list[j+1])
# 음수의 개수가 짝수면 두 수를 곱하고 정답에 더하기
else:
    for j in range(0, len(minus_list), 2):
        ans += (minus_list[j]) * (minus_list[j + 1])

# 수 1에 대한 계산
for j in range(len(one_list)):
    ans += one_list[j]

# 정답 출력
print(ans)
