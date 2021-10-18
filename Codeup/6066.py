def odd(n):
    if n % 2 != 0:
        return "odd"
    else:
        return "even"

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print(odd(a))
print(odd(b))
print(odd(c))