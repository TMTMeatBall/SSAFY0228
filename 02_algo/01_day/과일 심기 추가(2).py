T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    garden = [list(map(int, input().split())) for _ in range(N)]
    plants = []
    mxp_col = []
    for i in range(N):
        for j in range(0, M, 2):
            plants.append(garden[i][j])
    plant_expense = sum(plants)
    plant_num = len(plants)
    mxp = max(plants)

    for i in range(N):  # 최댓값이 있는 열번호들 싹 받기
        for j in range(0, M, 2):
            if mxp == garden[i][j]:
                mxp_col.append(j)

    mxp_col.sort()
    print(f'#{tc} {plant_expense} {plant_num} {mxp} {mxp_col[-1] + 1}')
