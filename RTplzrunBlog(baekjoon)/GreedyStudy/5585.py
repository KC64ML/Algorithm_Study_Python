import sys

read = sys.stdin.readline

money = int(read())

money = 1000 - money

dollar = [500,100,50,10,5,1]

answer = 0
calculated = 0

for in_d in dollar:
    answer += money // in_d
    money = money % in_d
    if not money:
        break

print(answer)