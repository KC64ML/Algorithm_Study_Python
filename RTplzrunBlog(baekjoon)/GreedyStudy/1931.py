import sys

read = sys.stdin.readline

n = int(read())

meetingroom = []

for i in range(n):
    meetingroom.append(list(map(int, read().split())))

meetingroom.sort(key=lambda x: (x[1],x[0]))

answer = 1
res = meetingroom[0][1]

for i in range(1, n):
    if res <= meetingroom[i][0]:
        res = meetingroom[i][1]
        answer += 1

print(answer)
