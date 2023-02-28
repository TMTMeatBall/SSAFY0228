dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]


def land_poss(x, y):
    land_place = arr[x][y]

    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M: #가로 N과 세로 M
            continue

        if arr[x][y] > arr[nx][ny]:
            cnt += 1

    if cnt >= 4:
        return True
    else:
        return False


T = int(input())
for tc in range(1,11):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    land_poss_candi = []
    for i in range(N):
        for j in range(M):
            result = land_poss(i, j)
            if result == True:
                land_poss_candi.append(arr[i][j])

    print(f'#{tc} {len(land_poss_candi)}')
