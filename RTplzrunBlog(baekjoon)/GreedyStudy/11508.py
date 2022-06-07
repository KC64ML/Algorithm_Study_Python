import sys

read = sys.stdin.readline

n = int(read())

product = []

for i in range(n):
    product.append(int(read()))

product.sort(reverse=True)

if len(product) % 3 != 0:
    product = product + [0] * (len(product) % 3)

answer = 0

for i in range(0, n, 3):
    answer += product[i] + product[i + 1]

print(answer)