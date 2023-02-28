# 범위를 기준으로 표시 후에 확산
# [1]집 좌표를 받아서
# [2]각 기준위치에서 거리를 표시(누적)
# cost[k]<-dist[k] * M:
# ans<-갱신
def solve_idea():
    mx = 0
    home = []
    for si in range(N):
        for sj in range(N):  # 집의 모든 위치를 받는다
            if arr[si][sj] == 1:
                home.append((si, sj))
    # 각 기준위치에서 거리별 집의 개수를 누적
    for si in range(N):
        for sj in range(N):
            dist = [0] * 40
            for ti, tj in home:
                t = abs(si, ti) + abs(sj - tj) + 1
                dist[t] += 1

            for k in range(1, 40):
                dist[k] += dist[k - 1]
                if cost[k] <= dist[k] * M:
                    mx = max(mx, dist[k])
