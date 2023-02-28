# ctrl alt L => 자동 정렬
N = 8
mazeArray = [[0, 0, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 0, 1, 1, 1, 1],
             [1, 1, 1, 0, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 0]]
# 막다른 곳에 다다르면 이동경로를 저장한 스택을 되돌려서
# 1. 사방 탐색이 가능하게 해야 함
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# dfs함수에 뭐가 필요할까?
# visited :방문했음을 체크한 배열
# stack.. <- 재귀호출로 최대한 처리(시스템스택)
visited = [[False] * N for _ in range(N)]


def dfs(visited, x, y):
    if x == N - 1 and y == N - 1:
        return True
    visited[x][y] = True
    result = False
    # 사방탐색을해서갈수있는위치가생기면
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 갈수있는위치인지체크
        if nx < 0 or ny < 0 or nx >= N or ny >= N or mazeArray[nx][ny] == 1 or visited[nx][ny] == True:
            continue
        # 그위치로dfs함수를재귀호출
        result = result or dfs(visited, nx, ny)
    # 사방탐색을 하여도 더 진행불가하다면, False
    return result


result = dfs(visited, 0, 0)
print(result)
