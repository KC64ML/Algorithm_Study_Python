import sys

read = sys.stdin.readline

e, s, m = map(int, read().split())

e_cnt = 0
s_cnt = 0
m_cnt = 0

result = 0

while True:

    if e_cnt == e and s_cnt == s and m_cnt == m:
        break

    e_cnt += 1
    s_cnt += 1
    m_cnt += 1
    result += 1

    if e_cnt > 15:
        e_cnt = 1

    if s_cnt > 28:
        s_cnt = 1

    if m_cnt > 19:
        m_cnt = 1

print(result)
