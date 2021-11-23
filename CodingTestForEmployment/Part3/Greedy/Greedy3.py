s = input()

before = 0
cnt_0 = 0
cnt_1 = 0

for idx in range(1, len(s)):
    if s[before] != s[idx] and s[before] == '0':
        cnt_0 += 1
        before = idx
    elif s[before] != s[idx] and s[before] == '1':
        cnt_1 += 1
        before = idx

if s[len(s)-1] == '0':
    cnt_0 += 1
else:
    cnt_1 += 1


if cnt_0 > cnt_1 :
    print(cnt_1)
else:
    print(cnt_0)