T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    garden = [list(map(int, input().split())) for _ in range(N)]
    plants = []
    mxp_col = []
    # 작물은 홀수 열에만 심게 된다.
    # for j in range(1, M + 1, 2):
    #     for i in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, M + 1, 2):
            plants.append(garden[i - 1][j - 1])
    plant_expense = sum(plants)
    plant_num = len(plants)
    mxp = max(plants)

    for i in range(1, N + 1):  # 최댓값이 있는 열번호들 싹 받기
        for j in range(1, M + 1, 2):
            if mxp == garden[i - 1][j - 1]:
                mxp_col.append(j)

    mxp_col.sort()
    print(f'#{tc} {plant_expense} {plant_num} {mxp} {mxp_col[-1]}')
