T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]  # arr받기
    crops = []  # 여기에 작물 심은 위치의 최종가치값을 전부 저장
    col = [0] * N
    for i in range(0, N):  # 0,1,2,3...N-1
        for j in range(0, M, 2):  # 0,2,4....M-1
            crops.append(arr[i][j])
    expense = sum(crops)
    crop_num = len(crops)
    crop_value = sorted(crops)
    crop_col = 0
    mx = max(crops)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == mx:
                crop_col = j
    print("#{} {} {} {} {}".format(tc, expense, crop_num, crop_value[-1], crop_col+1))