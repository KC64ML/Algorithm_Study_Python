for T in range(int(input())):
    P = input().rstrip()
    Q = input().rstrip()

    if P + "a" != Q:
        result = "Y"
    else:
        result = "N"

    print(f'#{T + 1} {result}')

# 왜 D3 인가.