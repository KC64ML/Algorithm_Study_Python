def solution(s):
    answer = 0
    total = ''
    result = ''

    for i in range(1, len(s) // 2 + 1):
        check_in_s = s[:i]
        cnt = 1
        result = ''

        # print("i : ",i,end = " ")
        for j in range(i, len(s), i):
            # print("j : ",j,end = " ")
            check_after_s = s[j:i + j]
            # print("after_s : ",check_after_s, end=" ")
            if check_in_s == check_after_s:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt) + check_in_s
                else:
                    result += check_in_s
                check_in_s = check_after_s
                cnt = 1
            # print("result : ",result, end=" ")
            # print()
        if cnt > 1:
            result += str(cnt) + check_in_s
        else:
            result += check_in_s

        # print("result : ",len(result), " ",result)
        # print()
        if total == '' or len(total) > len(result):
            total = result

    answer = len(total)

    if answer == 0:
        answer = 1

    return answer