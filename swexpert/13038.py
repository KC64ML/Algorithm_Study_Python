t = int(input())

answer = ''

for tc in range(1, t + 1) :
    n = int(input())
    data = list(map(int, input().split()))
    result = 1e9

    for i in range(7) :
        if data[i] == 1:
            index = i
            temp_n = n
            temp_result = 0

            while temp_n:
                if data[index] == 1:
                    temp_n -= 1
                temp_result += 1
                index = (index + 1) % 7

            if result > temp_result:
                result = temp_result

    answer += f'#{tc} {result} \n'

print(answer)