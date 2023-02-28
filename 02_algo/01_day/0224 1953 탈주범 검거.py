# BFS틀. 4방/범위내 조건->queue에 삽입 + 내가 이동할 방향 파이프에 연결이 있으면
# 연결되어 있으므로 이동할 수 있을 것
# p = [[][0,1,2,3][0,1][2,3][0,3][1,3][1,2][0,2]]
# 위의 배열은 각 인덱스에 따른 파이프가 어떻게 연결되어 있는지 인접 파이프를
# 배열 리스트로 뽑아낸 것
# 파이프의 종류 별 연결 수준을 그린 그림을 배열로 출력한 것
# 1번 파이프는 0123번(사방)과 연결되어 있고, 2번 파이프는 0,1(위아래)번과 연결되어 있음

# for dr in p[arr[ci][cj]] : 나의 연결방향
# ni,nj <- 계산한다 opp={0:1,1:0,2:3,3:2}
# 내가 이동할 파이프가, 나와 연결되어 있을까를 확인할 필요 있음
# if opp[dr]
# 내가 이동한 방향 파이프의 형태가, 나와 연결될 수 있는 형태인가
# if opp[dr] in p[arr[ni][nj]]:
# q삽입,v[n] <- v[c]+1
# cnt += 1 위치의 갯수를 더해준다
# 종료조건 : L
# 꺼냈을 떄에 ==L이라면,
# v[ci][cj]
p = [[], [0, 1, 2, 3][0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
opp = {0: 1}
di, dj = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(si, sj, L):
    q = []
    v = [[0] * M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        if v[ci][cj] == L:
            return cnt

        for dr in p[arr[ci][cj]]:
            ni, nj = ci + di[dr], cj + dj[dr]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and \
                    opp[dr] in p[arr[ni][nj]]:
                q.append((ni, nj))
                v[ni][nj] = v[]


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(R, C, L)
    print(f'{tc} {ans}')

