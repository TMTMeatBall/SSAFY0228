def sudoku(arr):
    for i in range(9):
        # 전체 0인 리스트에서 숫자에 해당하는 인덱스에 1씩 더함. 2가 있다면 스도쿠 아니므로 0 반환

        garo = [0] * 10
        sero = [0] * 10
        for j in range(9):
            garo[arr[i][j]] += 1  # 행 가져가는 법
            if garo[arr[i][j]] == 2:
                return 0
            sero[arr[j][i]] += 1  # 열 가져가는 법
            if sero[arr[j][i]] == 2:
                return 0

    for x in range(0, 9, 3):  # x : 0,3,6
        for y in range(0, 9, 3):  # y : 0 3 6
            cube = [0] * 10  # cube 는 9번 초기화 될 필요 있음
            for k in range(3):  # 012
                for l in range(3):  # 012
                    cube[arr[x + k][y + l]] += 1  # arr에 넣고 나온 값이 큐브의 idx값에 1씩 더함
                    # cube[arr[0+0][0+0]],cube[arr[0+0][0+1],cube[arr[0+0][0+2]\
                    # cube[arr[0+1][0+0]],cube[arr[0+1][0+1],cube[arr[0+1][0+2]\
                    # cube[arr[0+2][0+0]],cube[arr[0+2][0+1],cube[arr[0+2][0+2] ->1번 큐브
                    # cube[arr[0+0][3+0]],cube[arr[0+0][3+1],cube[arr[0+0][3+2]\...
                    if cube[arr[x + k][y + l]] == 2:
                        return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = sudoku(arr)
    print(f'#{tc} {result}')
