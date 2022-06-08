import sys


read = sys.stdin.readline

mk = read().rstrip()

bigresult = ''
smallresult = ''


cnt = 0
for in_mk in mk:
    if in_mk == 'K':
        bigresult += ('5' + '0'*cnt)
        cnt = 0
    else:
        cnt += 1

if cnt != 0:
    bigresult += ('1'*cnt)

cnt = 0
for in_mk in mk:
    if in_mk == 'K':
        if cnt >= 1:
            smallresult += ('1' + '0' * (cnt-1))
            cnt = 0
        smallresult += '5'
    else:
        cnt += 1

if cnt != 0:
    smallresult += ('1' + '0' * (cnt-1))

print(bigresult)
print(smallresult)
