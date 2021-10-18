def odd(n):
    if n % 2 != 0:
        return "odd"
    else:
        return "even"

a = input()
a = float(a)

if a < 0:
    if odd(a) == "even": print("A")
    else: print("B")
else:
    if odd(a) == "even":
        print("C")
    else:
        print("D")
