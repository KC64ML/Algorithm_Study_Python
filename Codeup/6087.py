n = int(input())


for date in range(1,n+1):
    if(date % 3 == 0):
        continue

    print("%d "%(date),end="")