t = int(input())

day = {'MON': 6, "TUE": 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1, "SUN": 7}

for i in range(t):
    s = input()
    print("#{} {}".format(i+1, day[s]))