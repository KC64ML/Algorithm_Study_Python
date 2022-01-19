# 열 개씩 끊어서 출력하기

alpabet = input()

reminder = len(alpabet) % 10

for i in range(0, len(alpabet), 10):
    print(alpabet[i:i+10])
