# 첫 줄에 테스트 케이스의 개수 T가 온다
T = int(input())
for tc in range(1, T + 1):

    totalarr = []

    result = 1

    for i in range(9):
        a = list(map(int, input().split()))
        totalarr.append(a)
    print(totalarr)
    for i in range(9):
        for j in range(9):
            diff_a = totalarr[i][j]
            for k in range(9):
                diff_b = totalarr[i][k]
                diff_c = totalarr[k][j]
                if k != i and k != j:
                    if diff_a == diff_b or diff_a == diff_c:
                        result = 0

    for i in range(3):
        for j in range(3):
            b = [list(map(int, input().split())) for _ in range(9)]
            tt_box = [0] * 10
            for k in range(3):
                for s in range(3):
                    tt_box[b[i * 3 + k][j * 3 + s]] = 1
                if sum(tt_box) != 9:
                    result = 0

    print(f'#{tc} {result}')
# 가로 검증
# 세로 검증
# 3*3에서의 검증
