a, d, n = input().split()

a = int(a)
d = int(d)
n = int(n)


for idx in range(1,n):
    a += d

print(a)

