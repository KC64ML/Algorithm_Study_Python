import sys

input = sys.stdin.readline


def merge(a, b):
    global cnt
    # 왼쪽, 오른쪽 길이를 구한다.
    la, lb = len(a), len(b)
    i, j = 0, 0

    # 결과 저장할 리스트
    temp = []

    # 왼쪽과 오른쪽 각각 작을 때
    while i < la and j < lb:
        # 만약 a에 있는 데이터가 b에 있는 데이터보다 클 때는 temp에 담는다.
        if a[i] > b[j]:
            temp.append(b[j])

            # j값을 한 칸 증가하고
            j += 1

            # 현재 i보다 j가 작다면 la가 왼쪽 총 길이니 현재 i까지 거리만큼 교환이 일어난다.
            cnt += la - i
        else:
            temp.append(a[i])
            i += 1
    if i == la:
        # i가 먼저 끝난 경우
        temp.extend(b[j:])
    else:
        # 아직 정렬이 안된 a들 이다. b보다 큰 값이 존재할 때 가능하다.
        temp.extend(a[i:])
    return temp

# 분할 정렬
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2

    # mid를 기준으로 돌린다.
    return merge(merge_sort(arr[left:mid + 1]), merge_sort(arr[mid + 1:]))


n = int(input())
cnt = 0
arr = list(map(int, input().split()))
merge_sort(arr)
print(cnt)

# https://cantcoding.tistory.com/33
