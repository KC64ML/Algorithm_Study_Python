n = int(input())

# n : 가로 길이

before_1 = 1
before_2 = 2

next_data = 0

if n == 1:
    print(before_1)
elif n == 2:
    print(before_2)
else:
    for _ in range(3, n + 1):
        next_data = (before_2 % 10007 + before_1 % 10007) % 10007
        before_2, before_1 = next_data, before_2

    print(next_data)
