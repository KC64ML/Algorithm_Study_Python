import sys

sys.setrecursionlimit(2 ** 9)

read = sys.stdin.readline

n = int(read())

card_A = list(map(int, read().split()))

card_A.sort()

m = int(read())

card_B = list(map(int, read().split()))


def binary_search(find):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if find == card_A[mid]:
            return 1
        elif find > card_A[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0


for find_data in card_B:
    print(binary_search(find_data), end=" ")
