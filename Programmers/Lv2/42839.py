def decimal_func(number):
    if number in (0, 1):
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True


def back_tracking(in_num, number_list, visited, result):
    if in_num not in result and decimal_func(int(in_num)):
        result.append(in_num)
    for i in range(len(number_list)):
        if not visited[i]:
            visited[i] = True
            back_tracking(in_num + number_list[i], number_list, visited, result)
            visited[i] = False


def solution(numbers):
    answer = []

    number_list = list(map(str, numbers.strip()))

    for in_num in number_list:
        if in_num == '0':
            continue
        else:
            visited = [False] * len(number_list)
            visited[number_list.index(in_num)] = True
            back_tracking(in_num, number_list, visited, answer)

    return len(answer)