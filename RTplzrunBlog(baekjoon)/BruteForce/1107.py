import sys

read = sys.stdin.readline

# 먼저 n을 입력 받는다.
n = int(read())

# 고장난 m을 입력받는다.
m = int(read())

remote_control = {str(num) for num in range(0, 10)}

# m이 0이 아닐 때 숫자를 입력받는다.
# - set메서드를 입력한 변수들을 변환하여 0 ~ 9에서 뺀다.
if m > 0:
    data2 = set(map(str, read().split()))
    remote_control -= data2

# N - 시작번호(100)을 뺀다. small_data : +- 로만 구할 때 총 경우의 수
min_result = abs(n - 100)

# 반복문을 돌리는데 이는 n이 40,000일 때 1, 2, 3, 4, 5를 입력할 수 없다면
# 60,000에서 -버튼 20,000을 눌리는게 베스트이다.
# 그러므로 범위는 50,000 * 2 = 100,000까지다.
# 전체 반복
# 1반복문 : 100,000 까지 숫자를 돌리면서
for cur_collect in range(1000000):
    for cur_collect_idx in range(len(str(cur_collect))):
        # 2반복문 : 라디오에 있는 버튼 크기만큼 돌리면서
        # - 만약, 현재 숫자가 라디오에서 누를 수 있는 숫자가 아니라면, 통과한다.
        if str(cur_collect)[cur_collect_idx] not in remote_control:
            break

        # - 만약, 전체 숫자가 누를 수 있는 번호라면
        # - small_data와 절대값(n - 현재 숫자를 누를 수 있는 번호: +-를 몇 번하는지) + 숫자 길이
        elif len(str(cur_collect)) - 1 == cur_collect_idx:
            min_result = min(min_result, abs(n - cur_collect) + len(str(cur_collect)))

print(min_result)





