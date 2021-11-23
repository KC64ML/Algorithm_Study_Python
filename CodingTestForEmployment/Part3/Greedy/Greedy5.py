# 무게가 1인 볼링공 : 1개
# 무게가 2인 볼링공 : 2개
# 무게가 3인 볼링공 : 2개


# A가 무게가 1인 공을 선택할 때의 경우의 수는
# 1 * 4 (2개 2개)
# A가 무게가 2인 공을 선택할 때의 경우의 수는
# 2 * 2 (2개)
# A가 무게가 2인 공을 선택할 때의 경우의 수는
# 2 * 0 (0개)


n, m = map(int,input().split())
datalist = list(map(int,input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in datalist:
    array[x] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)