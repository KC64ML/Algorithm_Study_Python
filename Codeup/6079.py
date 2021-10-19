num = int(input())
idx = 1
sum = 0

while True:
    sum += idx

    if num <= sum:
        print(idx)
        break
    idx += 1