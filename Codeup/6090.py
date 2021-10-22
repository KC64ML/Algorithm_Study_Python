a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

before = 1

for i in range(1,n+1):

    if(i > 1): a = before
    before = a * m + d


print(a)
