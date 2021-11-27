# 강의 영상 : https://youtu.be/RrWnBaflV2o

def match(arr, key, rot, r, c):
    n = len(key)
    for i in range(n):
        for j in range(n):
            # 회전 값이 없다면 그대로 복사한다.
            # 이외는 회전한다.
            if rot == 0:
                arr[r + i][c + j] += key[i][j]
            elif rot == 1:
                arr[r + i][c + j] += key[n - 1 - j][i]
            elif rot == 2:
                arr[r + i][c + j] += key[n - 1 - i][n - 1 - j]
            else:
                arr[r + i][c + j] += key[j][n - 1 - i]

def check(arr, offset, n):
    for i in range(n):
        for j in  range(n):
            if arr[offset+ i][offset + j] != 1:
                return False
    return True


def solution(key, lock):
    offset = len(key) - 1
    # key * key 크기의 사각형에서
    # offset은 겹치는 부분 제외 나머지 부분
    
    for r in range(offset + len(lock)):
        for c in range(offset + len(lock)):
            for rot in range(4):
                # 90도 방향으로 돌려본다. (4번을 돌리게 된다.)
                # 열쇠 같은 경우 최대 가로 20, 20, 20 세로 20, 20, 20
                # 최대한 하나는 겹쳐야 하므로 key 양쪽 끝 2개를 제외함으로
                # 60 - 2 = 58개가 필요하다.
                arr = [[0 for _ in range(58)] for _ in range(58)]
                # 자물쇠를 offset만큼 떨어진 위치에 복사한다.
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]

                # r, c, rot를 통하여 열쇠를 복사한다.
                match(arr, key, rot, r, c)
                if check(arr, offset, len(lock)):
                    return True
    return False


k = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]
solution(k, lock)
