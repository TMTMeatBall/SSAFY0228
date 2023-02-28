# N^2개의 방, 형태는 NxN
# 각 방의 번호가 1<= Aij <= N^2으로 기록됨
# 상하좌우에 있는 다른 방으로 이동
# 이동할 때에는 현재 내 방의 값 = 다음 방의 값 -1 이어야만 한다.
# 어떤 수가 적힌 방에서 가장 많은 개수의 방을 이동할 수 있을까?
# 전체를 순회! 미방문을 시작위치로
# arr[ci][cj] = arr[ni][nj] -1 (c = current, n = next)
# for si(N)
# for sj(N)
# if v[si][sj] == 0:
# 정답 갱신 <-  t,tcnt = bfs(si,sj)

# q,v, alst=[]
# q,v[si][sj],alst.append(arr[si][sj])
# while q:
# ci,cj <- pop

# 4방향,미방문*, 나랑 1 차이가 난다면,

# return min(alst),len(alst)
def bfs(si, sj):
    q = []
    alst = []

    q.append((si, sj))
    alst.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)

        # 4방향,미방문,조건 맞으면(1차이)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and \
                    abs(arr[ci][cj] - arr[ni][nj]) == 1:
                q.append((ni, nj))
                v[ni][nj] = 1
                alst.append(arr[ni][nj])
    return min(alst), len(alst)


T = int(input()) #tc 받기
for test_case in range(1, T + 1):
    N = int(input()) #정사각형 방의 크기
    arr = [list(map(int, input().split())) for _ in range(N)] #N*N어레이
    v = [[0] * N for _ in range(N)] #visited를 알 수 있게 0으로 이뤄진 배열
    ans, cnt = N * N, 0 #처음 출발할 방 번호, 몇 번 이동해야만 하는지
    for si in range(N):
        for sj in range(N):
            if v[si][sj] == 0:
                t, tcnt = bfs(si, sj)
                if cnt < tcnt or cnt == tcnt and ans > t:
                    ans, cnt = t, tcnt

    print(f'#{test_case} {ans} {cnt}')

#루프