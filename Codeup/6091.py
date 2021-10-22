a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

n = 1

while True:
    if n % a == 0 and n % b ==0 and n % c == 0:
        print(n)
        break

    n += 1