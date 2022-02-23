import math

a, b = map(int, input().split())
k = math.gcd(a, b)  # 정답은 k만큼의 1이 들어간 수가 되는 것
print('1' * k)
