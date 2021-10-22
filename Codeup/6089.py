a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

before = 1

for i in range(1,n+1):

    if(i > 1): a = before * r
    before = a


print(a)
