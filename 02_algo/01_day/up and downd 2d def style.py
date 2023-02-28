dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]


# 좌표 변화값 dx, dy는 고정이어야 하므로

def peakfinder(x, y):
    # 안쪽 사각형만을 돌도록 하는 범위 지정이 요구됨
    now_height = arr[x][y]

    cnt = 0 # 나보다_낮은_산_개수 = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        # if nx < 0 or ny < 0 or nx >= N or ny >= N:
        #     continue

        round_height = arr[nx][ny]
        if now_height > round_height:
            cnt += 1 #나보다_낮은_산_개수 += 1

    if cnt == 8: #나보다_낮은_산_개수 == 8:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    top_list = []
    for i in range(1,N-1):
        for j in range(1,N-1):
            result = peakfinder(i, j)
            if result == True:
                top_list.append(arr[i][j])

    top_list.sort()

    if len(top_list) <= 1:
        print(f'#{tc} -1')
    else:
        result = top_list[-1] - top_list[0]
        print(f'#{tc} {result}')
