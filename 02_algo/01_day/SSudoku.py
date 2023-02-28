N = int(input())
for tc in range(1, N+1):
    arr = [list(map(int,input().split())) for _ in range(9)] #2차원 배열
    garoarr = arr
    seroarr  = [[arr[i][j] for i in range(9)] for j in range(9)]
    miniarr = [[arr[i%3*3 + j//3][i//3*3 + j%3] for j in range(9)]for i in range(9)]
    result = 1
    for garo, sero, mini in zip(garoarr,seroarr,miniarr):
        if len(set(garo)) == len(set(sero)) == len(set(mini)) == 9:
            continue
        else:
            result = 0
            break
    print(f'#{tc} {result}')