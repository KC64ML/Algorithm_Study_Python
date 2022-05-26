from itertools import combinations

t = int(input())

for tc in range(1, t + 1):
    data = list(map(str, input()))
    target = [i for i in range(len(data))]
    # 배열의 인덱스 저장

    min_value, max_value = int(''.join(data)), int(''.join(data))

    for value in combinations(target, 2):
        # 2개의 조합을 이룬다.
        # print(value)
        i, j = value
        data[i], data[j] = data[j], data[i]
        # 0인 경우 스왑하지 않는다.
        if data[0] == '0':
            data[i], data[j] = data[j], data[i]
            continue

        # 제일 작은 것을 저장한다.
        if int(''.join(data)) < min_value:
            min_value = int(''.join(data))

        # 제일 큰 것을 저장한다.
        if int(''.join(data)) > max_value:
            max_value = int(''.join(data))
        data[i], data[j] = data[j], data[i]

    print('#%d %d %d' % (tc, min_value, max_value))
