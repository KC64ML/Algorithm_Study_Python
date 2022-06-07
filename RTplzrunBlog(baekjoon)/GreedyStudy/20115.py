import sys

read = sys.stdin.readline

n = int(read())

energy = list(map(int ,read().split()))

energy.sort(reverse=True)

answer = 0
answer += min(energy[0], energy[1]) / 2 + max(energy[0], energy[1])
for i in range(2, len(energy)):
    answer = min(answer, energy[i]) / 2 + max(answer, energy[i])

print(answer)
