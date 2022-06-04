import sys

read = sys.stdin.readline

t = int(read())

def in_solution(w, l, r):
    while l < r:
        if w[l] != w[r]:
            return False
        else:
            l += 1
            r -= 1
    return True

def solution(w, l, r):
    if w[:] == w[::-1]:
        return 0
    else:
        while l < r:
            if w[l] != w[r]:
                result1 = in_solution(w, l+1 , r)
                result2 = in_solution(w, l, r-1)

                if result1 or result2:
                    return 1
                else:
                    return 2
            else:
                l += 1
                r -= 1
        return 0


for i in range(t):
    alphabet = list(read().rstrip())
    left = 0
    right = len(alphabet) - 1
    answer = solution(alphabet, left, right)
    print(answer)


