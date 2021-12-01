
# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def corrected(u):
    count = 0 # 왼쪽 괄호의 개수
    for idx in range(len(u)):
        if u[idx] == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1

    return True # 쌍이 맞는 경우에 True 반환


def solution(p):
    answer = ''
    if p == '':
        return answer

    p_cur_index = balanced(p)
    u = p[:p_cur_index + 1]
    v = p[p_cur_index + 1:]

    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if (corrected(u)):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        # 만약 ( 없이 )이 먼저 시작된다면
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])  # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == ')':
                u[i] = '('
            else:
                u[i] = ')'

        answer += "".join(u)

    return answer

a = "()))((()"
b = ")("
print(solution(a))