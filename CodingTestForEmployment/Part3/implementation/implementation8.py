from itertools import permutations


def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1  # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        print()
        print("시작지점(start) : ", start)
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            print("friends : ", friends, end=' ')
            count = 1  # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            print("친구가 점검할 수 있는 마지막 위치 : ", position, ":", weak[start], "+", friends[count - 1])
            # 시작점부터 모든 취약 지점을 확인
            print("시작점 부터 모든 취약지점을 확인", start, start + length)
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    print("현재 index", index, "해당 친구가 점검할 수 있는 마지막 위치 < 취약한 지점 :", position, weak[index], end =' ')
                    count += 1  # 새로운 친구를 투입
                    print("새로운 친구를 투입")
                    if count > len(dist):  # 더 투입이 불가능하다면 종료
                        print("새로운 친구 명수가, 총 투입될 수 있는 인원수 보다 많아 종료")
                        break

                    position = weak[index] + friends[count - 1]
                    print("새로운 친구가 점검할 수 있는 마지막 위치 업데이트 : ", position,":",weak[index]," + ",friends[count-1], " index, count : ", index, count)
            answer = min(answer, count)  # 최솟값 계산
            print("결과 : ", answer)
    if answer > len(dist):
        return -1
    return answer


n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print("외벽의 길이 : ",n)
print("취약한 지점 : ",weak)
print("각 친구가 1시간 동안 이동할 수 있는 거리 ", dist)
print(solution(n, weak, dist))
