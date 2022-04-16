import sys

read = sys.stdin.readline

n = int(read())

a = []
b = []
c = []
d = []

for _ in range(n):
    x1, x2, x3, x4 = map(int, read().split())
    a.append(x1)
    b.append(x2)
    c.append(x3)
    d.append(x4)

abcd_sum = dict()

for in_a in a:
    for in_b in b:
        abcd_sum[in_a + in_b] = abcd_sum.get(in_a + in_b, 0) + 1

result = 0

for in_c in c:
    for in_d in d:
        result += abcd_sum.get(-(in_c + in_d), 0)

print(result)