def solution(N, stages):
    answer = []

    s_len = len(stages)

    sorted(stages)
    cur_data = 0
    total_data = s_len

    for idx in range(1, N + 1):
        # s_len 길이만큼 돌린다.
        # count로 확인하고 다음 턴 배열에서는 제외 시킨다. s_len에 나온 count 개수만큼 빼준다.
        cur_data = stages.count(idx)

        if cur_data == total_data:
            answer.append((1, idx))
        else:
            result = cur_data / total_data
            answer.append((result, idx))

        print("cur_data : ", cur_data, " total_data : ", total_data)

        total_data -= cur_data

    result = sorted(answer, key=lambda x: (-x[0], x[1]))
    print(result)
    return answer


solution(4, [1, 2, 3, 2, 1, 2])