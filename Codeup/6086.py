n = int(input())

idx = 1
sum = 0

while True:
    if n <= sum:
        break

    sum += idx
    idx +=1


print(sum)