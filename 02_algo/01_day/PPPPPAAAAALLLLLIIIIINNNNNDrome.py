# 제약사항
# aba도 회문, a도 길이 1짜리 회문
# 가로 또는 세로 직선인 회문만을 카운트
# 총 10개의 테스트 케이스가 주어진다
# 각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가, 다음 줄에는 8*8크기 글자판이 주어진다
# 출력은 #{tc} {회문개수} 로 출력한다.
for tc in range(1, 11):
    length = int(input())  # 회문의 길이
    board = []  # 8*8글자판
    for i in range(8):
        board.append(input())
    cnt = 0
    print(board)
    # 1.가로로 회문 찾기
    for i in range(8):
        for j in range(9 - length):
            a = board[i][j:j + length]
            if a == a[::-1]:
                cnt += 1
            else:
                cnt += 0
    # #2.세로로 회문 찾기
    for i in range(8):
        empty=''
        for j in range(9 - length):
            for k in range(length):
                empty += board[j+k][i]

                print(empty)
                if empty == empty[::-1]:
                    cnt += 1
                else:
                    cnt += 0

    #
    # print(f'#{tc} {cnt}')
