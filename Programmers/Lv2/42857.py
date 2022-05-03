from collections import deque


def solution(priorities, location):
    answer = 0

    q = deque([(v, i) for i, v in enumerate(priorities)])

    while len(q):
        cur_item = q.popleft()

        if q and max(q)[0] > cur_item[0]:
            q.append(cur_item)
        else:
            answer += 1
            if cur_item[1] == location:
                break

    return answer

solution([1, 1, 9, 1, 1, 1], 1)