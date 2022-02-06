n = int(input())

for idx in range(1, n):
    print(" " * (n - idx) + "*" * idx)
print("*"*n)
for idx in range(n + 1, 2 * n):
    print(" " * (idx - n) + "*" * (2 * n - idx))
