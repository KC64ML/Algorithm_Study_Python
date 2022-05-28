import math

tc = int(input())


def palindrome(num):
    sqrt_num = math.sqrt(num)

    if sqrt_num != int(sqrt_num):
        return False

    num = str(num)
    sqrt_num = str(int(sqrt_num))

    for k in range(len(num) // 2):
        if num[k] != num[len(num) - k - 1]:
            return False

    for k in range(len(sqrt_num) // 2):
        if sqrt_num[k] != sqrt_num[len(sqrt_num) - k - 1]:
            return False

    return True


answer = []

for i in range(1, tc+1):
    a, b = map(int, input().split())
    ret = 0

    for j in range(a, b + 1):
        if palindrome(j):
            ret += 1

    answer.append('#{} {}'.format(i, ret))

print('\n'.join(answer))
