import sys

read = sys.stdin.readline

ceremony = read().rstrip()

num = ''

check = False
start = False
for in_ceremony in ceremony:
    if '0' <= in_ceremony <= '9':
        if not start and in_ceremony == '0':
            continue
        else:
            num += in_ceremony
            start = True
    elif in_ceremony == '-':
        if not start:
            continue
        if not check:
            num += in_ceremony + '('
            check = True
        else:
            num += ')' + in_ceremony
            check = False

        start = False
    elif in_ceremony == '+':
        if not start:
            continue
        if check:
            num += in_ceremony
        else:
            num += in_ceremony

        start = False

if check:
    num += ')'

if num[-1] == '+' or num[-1] == '-':
    del num[-1]

print(eval(num))


# 참고하기 : https://pacific-ocean.tistory.com/228