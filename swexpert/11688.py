t = int(input())

for i in range(1, t+1):
    tree = list(map(str, input().rstrip()))
    a = 1
    b = 1

    for in_tree in tree:
        if in_tree == 'L':
            b = b + a
        else:
            a = a + b

    print('#{} {} {}'.format(i, a, b))