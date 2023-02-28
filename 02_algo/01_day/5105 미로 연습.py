def bfs(start_)


dx = [1,-1,0,0]
dy = [0,0,1,-1]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    adj = [[] for _ in range(N+1)]


    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_x = i
                start_y = j
            elif arr[i][j] == 3:
                end_x = i
                end_y = j

result = bfs(start_x,start_y,end_x,end_y)
print(f'#{tc} {result}')