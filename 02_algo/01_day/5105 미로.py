bfs탐색을 진행하되, 만나는 좌표가 (x,y) == (end_x,end_y) 하고 거리를 반영

visited 배열 또한 동일하게 이차원 배열을 요구함
visited배열
visited = [[False for _ in range(N)] for _ in range(N)]

results배열
results = [[0 for _ in range(N)] for _ in range(N)]
큐
q = deque()
q.append([start_x,start_y])
visited[start_x][start_y] = True
results[start_x][start_y] = 0
while q:
    node = q.popleft()
    cx, cy = q.popleft()
    if cx == end_x and cy == end_y:
        break
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        #배열 바깥을 벗어나거나 벽을 만난다면 continue
        if 0 > nx or 0 > ny or N <= nx or N <ny or arr[nx][ny] == 1:
            continue

        if visited[nx][ny] == True:
            continue

        q.append([nx,ny])
        visited[nx][ny] = True
        results[nx][ny] = result[cx][cy] +1
        완전탐색이 끝나면 while문을 빠져나올 것이므로
    return results[end_x][end_y] -1
#이상과 같이 짜면 이동할 때마다 갯수를 센 것이므로 -1 해준다
#start 가 end 와 동일 좌표일 때에는 0을 결과로 반환해야 한다.

탐색이 동서남북으로 늘었을 뿐 크게 바뀐 것은 없음
좀 많이 찾아서 풀어보길


dx = [-1,0,1,0]
dy = [0,-1,0,1]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    adj = [[] for _ in range(N+1)]
    print(arr)
    print(adj)
1벽
0은 통로
미로 밖으로 벗어나지 마라
2에서 출발해서
최소 몇 칸을 지나면 다다를 수 있는지를 출력
최소니까
BFS를 구현해서 찾아본다
입력받은 이후에
찾아야 할 것
시작점 2와 3에 대한 좌표 찾기
BFS순회의 끝은 2에서 3을 만나는 지점에 종료하면 된다
입력값 받기
미로의 크기N을 받고, 리스트 컴프리헨션으로 이차원 배열의 입력을 받는다
(input().split()과 input()의 차이)
도착지점과 출발지점에 대한 좌표 받기
start_x 로 변수지정 후 찾아보기
start_x
start_y
end_x
end_y
N*N배열을 모두 순회, 2값을 만나면 출발좌표,3은도착으로
순회를하게되면N만큼 이중으로 해야 전부 순회 가능
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            start_x = i
            start_y = j
        elif arr[i][j] == 3:
            end_x = i
            end_y = j

result = bfs(start_x, start_y, end_x,end_y)
print(f'#{tc} {result}')