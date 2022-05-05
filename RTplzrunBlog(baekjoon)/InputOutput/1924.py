x, y = map(int, input().split())

list_calendar = [[0] * 32 for _ in range(13)]

list_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

week_cnt = 0

for mon in range(1, 12 + 1):
    now_mon_day = 0
    if mon == 4 or mon == 6 or mon == 9 or mon == 11:
        now_mon_day = 30
    elif mon == 2:
        now_mon_day = 28
    else:
        now_mon_day = 31

    for day in range(1, now_mon_day + 1):
        list_calendar[mon][day] = list_week[week_cnt]

        week_cnt += 1

        if week_cnt == 7:
            week_cnt = 0

print(list_calendar[x][y])
