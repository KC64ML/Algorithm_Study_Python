import sys, math

read = sys.stdin.readline

n = int(read())

# s 초기 삼각형
star = ['  *  ', ' * * ', '*****']

# k는 문제에 나와있듯이, 3 x 2^k = N 이라는 것을 알 수 있다.
# k = N / 3 결과의 2의 지수이다.
k = int(math.log(n // 3, 2))


def makeUp(cur_k):
    # star 배열 크기만큼 반복문을 돌리면서 삽입하면 된다.
    cur_len = len(star)

    for i in range(cur_len):
        # k - 1 결과물을 좌, 우로 붙여주면 된다.
        # 층마다 결과물 쌓임
        star.append(star[i] + ' ' + star[i])

        # k가 증가할 수록 3*(k)칸찍 좌우로 빈공간이 생기는 것을 알 수 있다.
        star[i] = (' ' * 3) * cur_k + star[i] + (' ' * 3) * cur_k


# 그림을 보면
# k가 0인 경우, star 1개
# k가 1인 경우, star 3개, star 높이 : 2^1
# k가 2인 경우, star 9개, star 높이 : 2^2
# k가 3인 경우, star 27개, star 높이 : 2^3
# ~
for cur_num in range(k):
    makeUp(int(pow(2, cur_num)))

for i in range(n):
    print(star[i])
