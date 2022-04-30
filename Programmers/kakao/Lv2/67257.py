from itertools import permutations


def solution(expression):
    answer = 0

    oper = ['*', '+', '-']

    for perm in permutations(oper, 3):
        per = list(perm)
        temp = []
        emp = ''
        for i in range(len(expression)):
            # 숫자와 수학 기호를 분리한다.
            if str('0') <= expression[i] <= str('9'):
                emp += expression[i]
            else:
                temp.append(emp)
                temp.append(expression[i])
                emp = ''

            if i == (len(expression) - 1):
                temp.append(emp)
                emp = ''

        # 수학 기호를 돌리면서
        for p in perm:
            i = 0
            while i < len(temp):
                if p == temp[i]:
                    temp[i - 1] = eval(str(temp[i - 1]) + temp[i] + str(temp[i + 1]))

                    # 수학 기호 삭제
                    del temp[i]
                    if i < len(temp):
                        # 원래는 temp[i+1]인 숫자를 삭제 (위에서 del 한 번 했으므로, i번째를 삭제)
                        del temp[i]
                else:
                    i += 1
        answer = max(answer, abs(temp[0]))

    return answer