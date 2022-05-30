def solution(a, b):
    answer = ''
    week = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}

    day = [[''] * 40 for _ in range(13)]
    start = 5

    for i in range(1, 13):
        next_month_day = 31
        if i == 2:
            next_month_day = 29
        elif i == 4 or i == 6 or i == 9 or i == 11:
            next_month_day = 30

        for j in range(1, next_month_day + 1):
            day[i][j] = week[start]

            start += 1
            if start > 6:
                start = 0

    answer = day[a][b]

    return answer