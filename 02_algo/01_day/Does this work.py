# for t in range(1, 11) :
#     length = int(input())
#     board = []
#     for i in range(8) :
#         board.append(input())
#
#     count = 0
#     # 가로줄
#     for i in range(8) :
#         for j in range(9-length) :
#             answer = 1
#             for k in range(length//2) :
#                 if board[i][j+k] == board[i][j+length-k-1] :
#                     answer *= 1
#                 else :
#                     answer *= 0
#             if answer == 1 :
#                 count += 1
#     # 세로줄
#     for i in range(9-length) :
#         for j in range(8) :
#             answer = 1
#             for k in range(length//2) :
#                 if board[i+k][j] == board[i+length-k-1][j] :
#                     answer *= 1
#                 else :
#                     answer *= 0
#             if answer == 1 :
#                 count += 1
#     print("#{} {}".format(t, count))

for tc in range(1,11):
    length = int(input())
    arr = list(input() for i in range(8))
    result = 0

    # 가로 확인
    for j in range(8):
        for i in range(8 - length + 1):
            a = arr[j][i:i + length]
            if a == a[::-1]:
                result += 1

    # 세로 확인
    for j in range(8 - length + 1):
        # a=''#여기 두면 j가 초기화하는 때에 a가 한번 초기화되어 빈 문자열이 된다
        for i in range(8):
            a = ''#여기만 두는 이유? 언제 빈 문자열로 초기화하고 새로운 값을 띄우도록 하는가를 결정하는 데 사용
            for k in range(length):
                 # a= ''#여기 두면 k가 갱신될 때마다 a는 빈 문자열이 될 것이고,
                a += arr[j + k][i]
            if a == a[::-1]:
                result += 1
    print("#{} {}".format(tc, result))