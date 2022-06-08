# import sys
#
# read = sys.stdin.readline
#
# n = int(read())
#
# neighbor = list(read().rstrip())
#
# bcnt = 0
# rcnt = 0
#
# check = False
#
# for in_neighbor in neighbor:
#     if check and in_neighbor == 'B':
#         continue
#     elif (not check) and in_neighbor == 'B':
#         bcnt += 1
#         check = True
#     else:
#         check = False
#
# check = False
#
# for in_neighbor in neighbor:
#     if check and in_neighbor == 'R':
#         continue
#     elif (not check) and in_neighbor == 'R':
#         rcnt += 1
#         check = True
#     else:
#         check = False
#
# answer = min(bcnt, rcnt) + 1
#
# print(answer)


import sys

input = sys.stdin.readline

N = int(input())
s = input().rstrip()
cnt = {'B': 0, 'R': 0}
cnt[s[0]] += 1
for i in range(1, N):
    if s[i] != s[i - 1]:
        cnt[s[i]] += 1
print(min(cnt['B'], cnt['R']) + 1)
