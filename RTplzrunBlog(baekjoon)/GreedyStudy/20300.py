import sys

read = sys.stdin.readline

n = int(read())

exercise = list(map(int, read().split()))

exercise.sort()

answer = exercise[-1]

if len(exercise) % 2 != 0:
    del exercise[-1]

for i in range(len(exercise)//2):
    answer = max(answer, exercise[i] + exercise[len(exercise) - 1 - i])

print(answer)