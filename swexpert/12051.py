t = int(input())

for tc in range(1, t + 1):
    n, Pd, Pg = map(int, input().split())

    if Pd != 0 and Pg == 0:
        print('#%d %s' % (tc, 'Broken'))
    elif Pd != 100 and Pg == 100:
        print('#%d %s' % (tc, 'Broken'))
    else:
        flag = False
        for i in range(1, n + 1):
            if (i * Pd) / 100 == (i * Pd) // 100:  # 정수라면
                flag = True
                break

        if flag:
            print('#{} {}'.format(tc, 'Possible'))
        else:
            print('#%d %s' % (tc, 'Broken'))
