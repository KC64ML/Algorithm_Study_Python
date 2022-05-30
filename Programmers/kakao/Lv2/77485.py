def change_swap(x1, y1, x2, y2, arr):
    tmp = arr[x1 + 1][y1]
    result = arr[x1 + 1][y1]

    for k in range(x1 + 1, x2):
        arr[k][y1] = arr[k + 1][y1]
        result = min(result, arr[k + 1][y1])
    for k in range(y1, y2):
        arr[x2][k] = arr[x2][k + 1]
        result = min(result, arr[x2][k + 1])
    for k in range(x2, x1, -1):
        arr[k][y2] = arr[k - 1][y2]
        result = min(result, arr[k - 1][y2])
    for k in range(y2, y1, -1):
        arr[x1][k] = arr[x1][k - 1]
        result = min(result, arr[x1][k - 1])
    arr[x1][y1] = tmp
    return result


def solution(rows, columns, queries):
    answer = []

    arr = [[0] * (columns + 1) for _ in range(rows + 1)]

    in_d = 1

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            arr[i][j] = in_d
            in_d += 1

    for q in queries:
        answer.append(change_swap(q[0], q[1], q[2], q[3], arr))

    return answer
