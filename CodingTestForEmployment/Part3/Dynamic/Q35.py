n = int(input())

d = [1]


for num in range(2, 1001):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        d.append(num)

print(d[n-1])