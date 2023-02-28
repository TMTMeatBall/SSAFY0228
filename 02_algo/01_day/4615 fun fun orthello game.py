T = int(input())
for tc in range(1, T + 1):
    # 놓을 떄마다 8방향탐색을 뻗어나가면서 해야 한다.
    # visited 가 True 가 되었을 때에 체크를 하는 것처럼 뒤집어 준다?
    # 초기 배치의 입력부터?
    # arr[si][sj] = 초기 위치
    # 0 : break
    # 다른 돌을 만나면 뒤집어서 리스트에 넣어줄 필요 O temporary_list 에 넣어주는 것
    # 같은 돌을 만난 순간에, tlst안의 후보들을 전부 뒤집어서 다른 리스트로 옮겨준다.
    N, M = map(int, input().split())
    arr = [[0] * (N + 2) for _ in range(N + 2)]  # (N+2)*(N+2) 의 크기의 board(arr)
    # 초기의 돌 위치
    m = N // 2
    arr[m][m] = arr[m + 1][m + 1] = 2
    arr[m + 1][m] = arr[m][m + 1] = 1
    # 흑돌과 백돌의 입력과 처리
    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        for di, dj in ((-1 - 1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
    # 해당 방향으로 끝까지 뻗어나가게 해야 한다
            temp_lst = []
    for mul in range(1, N):
        ni, nj = si, di * mul, sj + dj * mul  # 빈칸의 범위 밖
        if arr[ni][nj] == 0:
            break
        elif arr[ni][nj] != d:  # 다른 돌인 경우 뒤집을 후보리스트에 넣는다
            temp_lst.append((ni, nj))
        else:  # 같은돌->후보돌을 전부 뒤집는 행동을 한다.
            while temp_lst:
                ti, tj = temp_lst.pop()
                arr[ti][tj] = d
            break
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)

    print(f'#{tc} {bcnt} {wcnt}')
