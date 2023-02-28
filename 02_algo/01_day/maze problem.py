# 1. NxN크기의 미로에서 출발지/목적지 도착하는 경로가 존재하는가를 확인하는 프로그램의 작성
# 2. 도착가능 시에는 1 그렇지 않으면 0을 출력
# 3. 미로 밖으로 나갈 수 없도록 작성
# 4. 시작점은 2 도착점은 4 벽은 1 통로는 0을 뜻한다.
# 탐색 함수를 만들자
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    for i in range(4):#4방탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            if maze[nx][ny] == '0':
                if dfs(nx, ny):
                    return True
            elif maze[nx][ny] == '3':
                return True
    return False


def search(N, maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                result = dfs(i, j)
                return 1 if result else 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(input().strip()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    print(f'#{tc} {search(N, maze)}')
# 5. 사방 탐색
# 6. 시작점 2 도착점 3의 지정
# 방문 노드가 해답이 될 수 없다면 뒤로 돌아간다.
# 시작점에서 한 방향으로 이동한 후에 갈 수 있을 때까지 stack에 push한다
# 벽에 막힌 경우 pop하면서 돌아온다
# 이동가능해질 떄까지 pop한 후에 다른 방향으로 이동한다.
