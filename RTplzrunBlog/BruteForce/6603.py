import sys
from itertools import combinations

read = sys.stdin.readline

while True:
    test_case = list(map(int, read().split()))
    if not test_case[0]:
        break

    k = test_case[0]
    s = test_case[1:]

    result = combinations(s, 6)

    for lotto in result:
        print(' '.join(map(str, lotto)))

    print()
