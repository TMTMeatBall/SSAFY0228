dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global is_check
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            if maze[nx][ny] == '3':
                is_check = True
            elif maze[nx][ny] == '0':
                dfs(nx, ny)

testCase = int(input())

for tc in range(1, testCase + 1):
    N = int(input())

maze = [list(input()) for _ in range(N)]
visited = [[False for _ in range(N)] for i in range(N)]

is_check = False
for i in range(N):
    for j in range(N):
        if maze[i][j] == '2':
            dfs(i, j)

if is_check:
    print(f"#{tc} 1")
else:
    print(f"#{tc} 0")