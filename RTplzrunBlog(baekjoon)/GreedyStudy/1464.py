import sys

read = sys.stdin.readline

s = list(read().rstrip())

ascii_code = []

for i in s:
    ascii_code.append(ord(i))

reverse = list()
tmp = ascii_code[0]
reverse.append(tmp)

for i in range(1, len(s)):
    if tmp < ascii_code[i]:
        reverse.reverse()
        reverse.append(ascii_code[i])
        reverse.reverse()
    else:
        tmp = ascii_code[i]
        reverse.append(ascii_code[i])

answer = ''

for i in reversed(reverse):
    answer += chr(i)

print(answer)

