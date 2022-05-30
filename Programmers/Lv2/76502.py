from itertools import permutations

def solution(s):
    answer = -1
    s = list(s)
    a = list(map(''.join, permutations(s)))
    print(a)
    return answer

t = "[](){}"

solution(t)