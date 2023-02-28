#bfs를 4방향,범위내,미방문, cnt+=1
#v[ci][cj]가 변경될 때에 정답을 갱신해준다
def(si,sj):
    q=[]
    v=[[0]*N for _ in range(N)]
    old = 0

    q.append((si,sj))
    v[si][sj] = 1
    cnt = arr[si][sj] #시작 좌표가 집->1, 시작 좌표가 그 외에는 0

    while q:
        ci,cj = q.pop(0)
        if old != v[ci][cj]: #k값이 달라진 경우

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0 <= nj < N and v[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1
                cnt += arr[ni][nj]

def solve_bfs():
    mx = 0
    for si in range(N):
        for sj in range(N):
            mx = max(mx,bfs(si,sj))
    return mx