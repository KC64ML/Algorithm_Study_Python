tc = int(input())

for i in range(1, tc + 1):
    s = input()

    answer = "No"

    for j in range(0, 3):
        if s[j] != s[j+1]:
            if s.count(s[j]) == 2:
                answer = "Yes"
            else:
                answer = "No"
                break
    print("#{} {}".format(i, answer))

