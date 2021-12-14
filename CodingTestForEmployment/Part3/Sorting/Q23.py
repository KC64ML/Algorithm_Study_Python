# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키코드에서 대문자는 소문자보다 작으므로 사전 순으로 앞에 온다.)

n = int(input())

list_data = []

# list에 tuple 입력하기
for _ in range(n):
    list_data2 = list(input().split())

result = sorted(list_data, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for idx in range(len(result)):
    print(result[idx][0])