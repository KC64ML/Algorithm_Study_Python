# u가 올바른 괄호인지 판단하는 함수
def collect_u(u):
    left, right = 0, 0
    for i in u:
        if i == '(':
            left += 1
        else:
            right += 1

        if left < right:
            return False
    return True


# dfs
def dfs(arr):
    if len(arr) == 0:
        return ''
    u, v = [], []
    left, right = 0, 0
    check = False

    # u, v 값을 찾기 위한 반복문
    for alpa in arr:
        if alpa == '(':
            left += 1
        else:
            right += 1

        if not check:
            u.append(alpa)
        else:
            v.append(alpa)

        if left == right:
            check = True

    # u가 올바른 괄호인지 판단한다.
    if collect_u(u):
        u = ''.join(u)
        return ''.join(u + dfs(v))
    else:
        r = '('
        r += dfs(v)
        r += ')'
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                r += ')'
            else:
                r += '('
        return r


def solution(p):
    answer = dfs(p)
    return answer
