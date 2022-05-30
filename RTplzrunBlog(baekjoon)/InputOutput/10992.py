n = int(input())

print(" " * (n - 1) + "*")

for idx in range(2, n):
    print(" " * (n - idx) + "*" + " " * (2 * (idx - 1) - 1) + "*")

if n != 1:
    print("*" * (2 * n - 1))
