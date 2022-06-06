import sys

read = sys.stdin.readline

board = read().rstrip()
board += ' '
# 한 라인 더가서 구해질수도 있다.
cnt = 0
answer = ''
for i in range(len(board)-1):
    if board[i] == 'X':
        cnt += 1
    if board[i] == '.':
        answer += '.'
        # 2의 배수가 아니라면
        if cnt % 2 != 0:
            break
        else:
            cnt = 0

    if cnt == 2 and board[i+1] != 'X':
        answer += 'BB'
        cnt = 0
    elif cnt == 4:
        answer += 'AAAA'
        cnt = 0

if cnt % 2 == 1:
    print('-1')
else:
    print(answer)
