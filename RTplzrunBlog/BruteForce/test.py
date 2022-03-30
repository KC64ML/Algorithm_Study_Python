# n, m = map(int, input().split())
#
# # 입력받은 전체 직사각형을 저장하기 위한 리스트(편리한 인덱싱을 위해 행 삽입)
# rectangle_input = [[0 for _ in range(m + 1)]]
#
# for _ in range(n):
#     # 라인별로 읽고 rectangle_input에 저장(편리한 인덱싱을 위해 [0] 삽입)
#     line_input = [0] + list(map(int, list(input())))
#     rectangle_input.append(line_input)
#
# # 답은 최댓값을 출력해야 하므로, 0으로 시작
# ans = 0
#
# # 합을 저장할 리스트
# s = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
#
#
# print(rectangle_input)
#
# # 리스트 s는 입력받은 직사각형의 1,1부터 영역 내 모든 수의 합을 저장
# for row in range(1, n + 1):
#     for col in range(1, m + 1):
#         s[row][col] = s[row - 1][col] + s[row][col - 1] - s[row - 1][col - 1] + rectangle_input[row][col]
#         print("행, 열 : ", row, col, " : ", " s[row-1][col] ",s[row-1][col], "+ s[row][col-1]",s[row][col-1],
#               "- s[row - 1][col - 1] : " , s[row - 1][col - 1] , "+ rectangle_input[row][col] ", rectangle_input[row][col], end=" ")
#         print("결과 : ",s[row][col])
#
#
# print(s)