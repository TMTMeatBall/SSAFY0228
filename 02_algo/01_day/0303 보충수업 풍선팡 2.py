# 결국 상하좌우 탐색해서 터트린다 했을 때에 nx,ny가 범위를 넘지 않게 하는 것 잊지 말기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp = arr[i][j]
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0<=ni<N and 0<=nj<M:
                    tmp += arr[ni][nj]

            if cnt < tmp:
                cnt = tmp

    print(f'#{tc} {cnt}')
