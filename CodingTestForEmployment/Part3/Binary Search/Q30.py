def binary_Search(w, q):
    if len(w) == 1 or len(q) == 1:
        return False
    else:
        # q의 앞이 ?로 시작하는지
        q_next_start = 0
        q_next_end = len(q) - 1
        if q[0] == '?':
            q_next_start = (len(q) // 2)
        else:
            q_next_end = (len(q) // 2)
        print(q[q_next_start:q_next_end])
        binary_Search(w[q_next_start:q_next_end], q[q_next_start:q_next_end])


def solution(words, queries):
    answer = []

    for i in range(len(words)):
        for j in range(len(queries)):
            if len(words[i]) != len(queries[j]):
                continue
            else:
                binary_Search(words[i], queries[i])

    return answer


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
