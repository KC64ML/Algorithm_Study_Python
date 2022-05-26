t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print("#{} {}".format(i+1, (a + b) % 24))
