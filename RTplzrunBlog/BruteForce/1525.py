import sys
from collections import deque

read = sys.stdin.readline

x_coordinate = [-1, 0, 1, 0]
y_coordinate = [0, 1, 0, -1]
table = ''

# 아홉 개의 수를 입력 받는다.
for _ in range(3):
    s = read()
    s = s.replace(' ', '')
    table += s.strip()


# bfs
def bfs():
    q = deque()
    q.append((table, 0))

    # 딕셔너리로, 방문한 지 안한지 key 값으로 판단한다.
    visited = dict()
    visited[table] = 1

    while q:
        # 퍼즐 9자리와, 현재 방문한 퍼즐 키 갯수를 확인한다.
        cur_puzzle, cur_cnt = q.popleft()

        # 찾았으면 끝!
        if cur_puzzle == '123456780':
            return cur_cnt

        # 0 인덱스를 찾는다.
        zero_index = cur_puzzle.index('0')
        cur_x = zero_index // 3  # 행
        cur_y = zero_index % 3  # 열

        # 상하좌우로 이동할 수 있는 곳 찾기
        for i in range(4):
            next_x = cur_x + x_coordinate[i]
            next_y = cur_y + y_coordinate[i]

            # 퍼즐 안이라면
            if 0 <= next_x < 3 and 0 <= next_y < 3:
                # 퍼즐은 일차원 배열에 저장할꺼기 때문에 (3 * 행 + 열)
                next_zero_index = next_x * 3 + next_y

                # list로 변환하여 해당 인덱스 값들을 교환한다.
                # str로 할 시 안됨!
                ct = list(cur_puzzle)
                ct[zero_index], ct[next_zero_index] = ct[next_zero_index], ct[zero_index]

                # 다시 list -> str로 자료형 변환한다.
                # 딕셔너리에서는 str을 key 값으로 가지고 있기 때문이다.
                so_next_puzzle = ''.join(ct)
                # 방문한 적 없는 곳이라면
                if not visited.get(so_next_puzzle):
                    # 방문 표시
                    visited[so_next_puzzle] = 1
                    # queue에 삽입한다.
                    q.append((so_next_puzzle, cur_cnt + 1))

    return -1


print(bfs())
