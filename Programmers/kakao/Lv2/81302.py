# 상하좌우
x_coordinate = [-1, 0, 1, 0]
y_coordinate = [0, 1, 0, -1]

# 대각선
x_diagonal = [-1, -1, 1, 1]
y_diagonal = [-1, 1, 1, -1]


def check_place(place):
    arr = []
    for i in range(len(place)):
        arr.append(list(map(str, place[i].strip())))

    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'P':
                # 상하좌우 체크
                for rc in range(4):
                    next_x = x_coordinate[rc] + i
                    next_y = y_coordinate[rc] + j

                    next_next_x = x_coordinate[rc] * 2 + i
                    next_next_y = y_coordinate[rc] * 2 + j

                    if 0 <= next_x < 5 and 0 <= next_y < 5:
                        if arr[next_x][next_y] == 'P':
                            return False
                        if arr[next_x][next_y] == 'O' and 0 <= next_next_x < 5 and 0 <= next_next_y < 5:
                            if arr[next_next_x][next_next_y] == 'P':
                                return False

                for rc in range(4):
                    next_x = x_diagonal[rc] + i
                    next_y = y_diagonal[rc] + j

                    if 0 <= next_x < 5 and 0 <= next_y < 5 and arr[next_x][next_y] == 'P':
                        if arr[next_x][j] == 'O':
                            return False

                        if arr[i][next_y] == 'O':
                            return False
    return True


def solution(places):
    answer = []

    for in_place in places:
        answer.append(int(check_place(in_place)))

    return answer