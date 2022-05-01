from collections import Counter


def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(',')) # ,을 기준으로 잘라서 넣기
    print(new_s)
    new_s.sort(key=len)
    t = sum(new_s, [])
    t_dic = Counter(t)
    answer = list(map(int, list(t_dic.keys())))
    return answer

solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
a = [2, 1, 3]

a.sort(reverse=True)



