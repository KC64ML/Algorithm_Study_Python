import sys

read = sys.stdin.readline

n = int(read())

card_A = list(map(int, read().split()))

dic_A = dict.fromkeys(card_A, 0)

for i in card_A:
    dic_A[i] += 1

m = int(read())

card_B = list(map(int, read().split()))

for num in card_B:
    result = dic_A.get(num)

    if not result:
        print(0, end=" ")
    else:
        print(result, end=" ")

