# N^2크기의 도시
# 운영 비용 = k*k + (k-1)*(k-1)
# 회사가 손해없이 운영가능한 집의 최대 갯수? K(요금)
# si.sj = start[i], start[j]
# ci,cj = current[i] current[j]
# ni,nj = next[i] next[j]
cost = [((k*k)+(k-1)*(k-1)) for k in range(40)]
def solve_loop():
    mx = 0
    for si in range(N):
        for sj in range(N):
            for k in range(1, 2 * N):
                cnt = 0
                for i in range(si - k + 1, si + k):
                    t = abs(si - i)
                    for j in range(sj - k + 1 + t, sj + k - t):
                        cnt += arr[i][j]
            #운영비용보다 수익이 같거나 클 때에 정답을 갱신
            # if ((k*k)+(k-1)*(k-1)) <= cnt*M:
                if cost[k] <= cnt*M
                mx = max(mx,cnt)
    return mx

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = solve_loop()
print(f'#{tc} {ans}')
