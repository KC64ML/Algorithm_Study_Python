def solution(record):
    answer = []
    cur_id_inout = []
    dist = {}
    record_list = []

    # 문자열 입력 : EnterLeaveChange, 유저아이디, 닉네임
    for in_record in record:
        record_list.append(in_record.split(' '))

    # 입력된 문자열 만큼 반복문을 돌린다.
    for i in range(len(record_list)):
        # 첫 번째 입력 값이 Enter이면
        if record_list[i][0] in 'Enter':
            # 유저아이디와 Enter 표시 를 list에 저장
            cur_id_inout.append((record_list[i][1], 1))
            # 딕셔너리 key로는 유저아이디 value로는 닉네임
            dist[record_list[i][1]] = record_list[i][2]
        elif record_list[i][0] in 'Leave':
            # leave라면 유저아이디와 leave 표시를 list에 저장
            cur_id_inout.append((record_list[i][1], -1))
        else:
            # change라면 key 유저아이디에 대한 value를 변경한다.
            dist[record_list[i][1]] = record_list[i][2]

    for name, eorl in cur_id_inout:
        if eorl == 1:
            answer.append(dist[name] + "님이 들어왔습니다.")
        else:
            answer.append(dist[name] + "님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
