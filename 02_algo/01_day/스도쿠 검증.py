# 검증하는 함수를 만들 수 있을까?
def check(exp):
    for i in range(9):
        row_code = [0] * 10
        col_code = [0] * 10
        for j in range(9):
            row = exp[i][j]
            col = exp[j][i]

            if row_code[row]:
                return 0
            if col_code[col]:
                return 0

            row_code[row] = 1
            col_code[col] = 1

            if i % 3 == 0 and j % 3 == 0:
                cube = [0] * 10
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        a = exp[k][l]
                        if cube[a] :
                            return 0
                        cube[a] = 1



T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = check(arr)

    print(f'#{tc} {result}')

# 1. 가로 검증
# 2. 세로 검증
# 3. 작은 사각형 검증
# 세 경우 모두에서 문제가 없을 경우에 1을 출력하고, 그렇지 않은 경우 0 을 출력

# arr[0][0] 부터 arr[0][8]에서 중복 없이
# 같은 방식으로 [8][0] [8][8]까지
# arr[0][0] 부터 arr[8][0]
