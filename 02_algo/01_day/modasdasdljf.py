def move(a):
    global x, y, di, ans
    if a == 0 and y+1 < N:
        ans.append(di[x][y])
        di[x][y] = -1 # 방문처리 -1
        y += 1
    elif a == 1 and x+1 < N:
        ans.append(di[x][y])
        di[x][y] = -1 # 방문처리 -1
        x += 1
    elif a == 2 and 0 <= y-1:
        ans.append(di[x][y])
        di[x][y] = -1 # 방문처리 -1
        y -= 1
    elif a == 3 and 0 <= x-1:
        ans.append(di[x][y])
        di[x][y] = -1 # 방문처리 -1
        x -= 1
    else:
        return -2
    if di[x][y] == -1:
        return -2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    di = [list(map(int, input().split())) for _ in range(N)]
    x = y = 0
    ans = []
    while True:
        if move(di[x][y]) == -2:
            break

    print(f'#{tc}', *ans)