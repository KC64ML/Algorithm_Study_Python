import sys

sys.setrecursionlimit(2 ** 8)

read = sys.stdin.readline

n = int(read())

bubble = list(map(int, read().split()))

result = 0


def quick_sort(arr):
    global result

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_node = [x for x in tail if x < pivot]
    right_node = [x for x in tail if x > pivot]

    result += (len(left_node) + len(right_node))

    return quick_sort(left_node) + [pivot] + quick_sort(right_node)


quick_sort(bubble)
print(result)


# 참고 자료 : https://cantcoding.tistory.com/33