def solution(numbers, hand):
    answer = ''
    dist = {i: [] for i in range(0, 10)}
    dist[0] = [3, 1]

    cnt = 1

    for i in range(3):
        for j in range(3):
            dist[cnt] = [i, j]
            cnt += 1

    # 첫 시작 위치
    cur_left = [3, 0]
    cur_right = [3, 2]
    for num in numbers:
        if num in [1, 4, 7]:
            # 왼쪽 좌표
            cur_left = [dist[num][0], dist[num][1]]
            answer += "L"
        elif num in [3, 6, 9]:
            # 오른쪽 좌표
            cur_right = [dist[num][0], dist[num][1]]
            answer += "R"
        else:
            # 가운데 있는 좌표
            cur_left_len = abs(cur_left[0] - dist[num][0]) + abs(cur_left[1] - dist[num][1])
            cur_right_len = abs(cur_right[0] - dist[num][0]) + abs(cur_right[1] - dist[num][1])
            if cur_left_len == cur_right_len:
                if hand == "right":
                    cur_right = [dist[num][0], dist[num][1]]
                    answer += "R"
                else:
                    cur_left = [dist[num][0], dist[num][1]]
                    answer += "L"
            else:
                if cur_left_len > cur_right_len:
                    cur_right = [dist[num][0], dist[num][1]]
                    answer += "R"
                else:
                    cur_left = [dist[num][0], dist[num][1]]
                    answer += "L"

    return answer
