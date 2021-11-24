s = input()

alpa = []
sum = 0

for i in range(len(s)):
    if '1' <= s[i] and s[i] <= '9':
        sum += int(s[i])
    else:
        alpa.append(s[i])

alpa.sort()
alpa.append(str(sum))
print(''.join(alpa))