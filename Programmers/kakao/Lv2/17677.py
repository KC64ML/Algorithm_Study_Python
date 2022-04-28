from collections import Counter


def solution(str1, str2):
    answer = 0

    # (1) str1, str2
    str1 = str1.upper()
    str2 = str2.upper()

    str_alpha = []
    str2_alpha = []
    # (2) 리스트에 알파벳 저장하기
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str_alpha.append(str1[i] + str1[i + 1])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_alpha.append(str2[i] + str2[i + 1])

    Counter1 = Counter(str_alpha)
    Counter2 = Counter(str2_alpha)
    # Counter.element() : Counter된 숫자만큼 요소들을 리턴
    a = list((Counter1 & Counter2).elements())
    b = list((Counter1 | Counter2).elements())

    if not len(a) and not len(b):
        answer = 65536
    else:
        answer = int(len(a) / len(b) * 65536)

    return answer