import sys

read = sys.stdin.readline

alpha = read().rstrip()
find_alpha = read().rstrip()
answer = 0
i = 0

while i < len(alpha):
    if alpha[i] == find_alpha[0]:
        check = True
        for j in range(1, len(find_alpha)):
            # i + j 가 alpha길이보다 크다면 종료
            if i + j >= len(alpha):
                check = False
                break

            # 현재 찾고자 하는 알파벳이 다음 인덱스 위치에 없을 때 종료
            if alpha[i + j] != find_alpha[j]:
                check = False
                break

        if check:
            # 찾았으면, 찾는 문자열 길이만큼 인덱스에 더해준다.
            i += len(find_alpha)
            answer += 1
        else:
            i += 1
    else:
        i += 1
print(answer)
