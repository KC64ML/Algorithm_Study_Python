from sys import stdin as s

n = int(s.readline())

dic = {}

for _ in range(n):
    card = int(s.readline())

    if card in dic:  # 딕셔너리안에 이미 card가 존재한다면
        dic[card] += 1
    else:  # 아니라면
        dic[card] = 1

result = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])
