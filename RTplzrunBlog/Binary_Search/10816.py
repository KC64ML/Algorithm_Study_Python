import sys
from collections import Counter

read = sys.stdin.readline

n = int(read())

card_A = list(map(int, read().split()))

m = int(read())

card_B = list(map(int, read().split()))

count = Counter(card_A)

print(' '.join(str(count[x]) if x in count else '0' for x in card_B))
# card_B에서 데이터를 꺼낸다. x가 count 안에 있다면 출력을 count[x]로 하고, 아니면 0을 한다.

# 참고 : https://www.acmicpc.net/source/38112063