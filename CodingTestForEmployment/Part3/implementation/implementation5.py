from collections import deque
n = int(input())

array = [[0] * (n+1) for i in range(n+1)]
k = int(input())

while True:
    if k < 1: break
    x, y = map(int, input().split())
    array[x][y] = 2
    k -= 1

l = int(input())
queue_x_c = deque([]) # 꼬리 위치 넣기

while True:
    if l < 1: break
    x, c = input().split()
    queue_x_c.append([x,c])
    l -= 1


snail_loc = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

snail_idx = 0 # 0 ~ 3
queue = deque([]) # 꼬리 위치 넣기
x, y = 1, 1
time = 0
snail_len = 1
cur_sec = queue_x_c.popleft()
before_list = []
tail_data = False

while True:


    # 게임 시작, 이동 자리 1로 대체
    array[x][y] = 1
    b_left = x
    b_right = y
    x += snail_loc[snail_idx][0]
    y += snail_loc[snail_idx][1]
    time += 1

    # print("x: ",x,  " y : ", y, " time : ",time)
    if x == 0 or y == 0 or x > n or y > n:
        break
    # 만났을 때 종료
    if array[x][y] == 1:
        break



    # 만약 사과가 있는 위치라면 deque 삽입
    # queue 삽입 알아보기
    if array[x][y] == 2:
        if tail_data is False and len(queue) == 0:
            queue.append([b_left, b_right])
            tail_data = True
        queue.append([x, y])

    else:
        tail_data = False
        # 만약 deque가 비어있지 않다면
        if len(queue) > 0:
            before_list = queue.popleft()
            b_left = before_list[0]
            b_right = before_list[1]
            queue.append([x, y])
        array[b_left][b_right] = 0

    if int(cur_sec[0]) == time:
        if cur_sec[1] == 'L':
            snail_idx -= 1
            if snail_idx == -1:
                snail_idx = 3
        else:
            snail_idx += 1
            if snail_idx == 4:
                snail_idx = 0
        if len(queue_x_c) > 0:
            cur_sec = queue_x_c.popleft()


# print("결과 ")
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(array[i][j], end = ' ')
#     print()

print(time)