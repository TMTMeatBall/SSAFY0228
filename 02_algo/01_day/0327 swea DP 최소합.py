T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    #오른 쪽 또는 아래만을 살피고 memoization 하고 연산에 집어넣는다.
    #중간위치 (i,j)까지의 최소 합을 구하는 방법
    #중간위치 (i,j)까지의 합을 반복하지 않도록 기억
    for i in range(n):
        for j in range(n):
            #위,왼쪽 두 방향에서 올 수 있음.
            if i - 1>=0 and j-1 >= 0:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1] )+arr[i][j]

            #경우의 수를 쪼개서 하면 된다.
            #위에서만 오는 경우
            elif i-1>=0 and j-1<0:
                dp[i][j] = dp[i-1][j] + arr[i][j]


            #왼쪽에서만 오는 경우

            elif i-1<0 and j-1>=0 :
                dp[i][j] = dp[i][j-1] + arr[i][j]

            #0짜리 리스트 그리고 이차원 리스트 만들어서 넣어줄 준비 하기
            #경우의 수 따지기
    print(f'#{tc} {dp[n-1][n-1]}')
