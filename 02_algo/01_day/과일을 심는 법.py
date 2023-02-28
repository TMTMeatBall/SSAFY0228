T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]  # arr받기
    crops = []  # 여기에 작물 심은 위치의 최종가치값을 전부 저장
    col = [0] * N
    for i in range(N):  # 0,1,2,3...N-1
        for j in range(0, M, 2):  # 0,2,4....M-1
            crops.append(arr[i][j])

    result_col = []
    expense = 0
    crop_num = 0
    crop_value = []
    crop_col = []
    for i in range(len(crops)):
        expense += crops[i]

    crop_num = len(crops)

    for i in range(len(crops)):
        crop_value.append(crops[i])

    crop_value.sort()

    mx = max(crops)
    for i in range(N):
        for j in range(0, M, 2):
            if mx == arr[i][j]:
                crop_col.append(j)  # 열 번호는 0부터 세었으므로 1 더해줘야 함
    crop_col.sort()
    print(f'#{tc} {expense} {crop_num} {crop_value[-1]} {crop_col[-1]+1}')
    # 저격당했음
    # col.append((arr[i][j],j))

    # best_value = 0
    # for i in crops:
    #     if best_value < i:
    #         best_value = i#i 최대값 찾기를 하면서 j값도 같이 받는다?

    # for i in range(len(crops)): #len(crops)로 갯수를 돌림
    #     if best_value < crops[i]:
    #         best_value = crops[i] #이상의 방식으로 최대 가치 작물을 구함
    #         print(i % M) #i 를 나눈 몫이 행을 표현하도록, i를 나눈 나머지가 열이 되도록
