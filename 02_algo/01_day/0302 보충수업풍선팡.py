T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            tmp = arr[i][j]
            cnt = arr[i][j]
            for k in range(1, tmp + 1):
                # up
                if i - k >= 0:
                    cnt += arr[i - k][j]
                # down
                if i + k < N:
                    cnt += arr[i + k][j]
                # left
                if j - k >= 0:
                    cnt += arr[i][j - k]
                # right
                if j + k < M:
                    cnt += arr[i][j + k]
            result = max(cnt, result)
    print(f'#{tc} {result}')

            # for k in range(4):
            #
            #     nx = i + dx[k]
            #     ny = j + dy[k]
            #     if 0 <= nx < N and 0 <= ny < M :
            #
            #         tmp += arr[nx][ny]
            #
            # if cnt < tmp:
            #     cnt = tmp

    # arr[i][j]가 찍혔을 떄에 arr[nx][ny]는
