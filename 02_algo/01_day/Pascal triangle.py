T = int(input())
for tc in range(1,T+1):
    print(f'#{tc}')
    N = int(input())
    p = []#파스칼의 삼각형 토털값
    for i in range(N):
        temp = [] #1개 행의 배치 열을 가로로 채워가는 한줄이므로 초기화 위치가 j가 변하는 바로 위
        for j in range(i + 1): #i+1 인 이유는 i번째 행에서는 i개만큼의 숫자가 필요 단 리스트->0부터 세므로 i+1로 세어야 한다
            if i == j or j == 0:
                temp.append(1)
            else:
                temp.append(p[i-1][j] + p[i-1][j-1]) #한 행 위의 요소 + 1행 1열 위의 요소 == 현재의 [i][j]에서의 요소
        p.append(temp)
    for i in p:#전체 받은 p를 출력하기
        print(*i) # *를 통해 리스트 안의 내용만을 출력 가능



#
# T = int(input())
# for tc in range(1, T + 1):
#     print(f'#{tc}')
#     N = int(input())
#     P = []
#     for i in range(N):
#         temp = []
#         for j in range(i + 1):  # i개 행에서 j개의 열을 출력하기 위해서 i+1 한다
#             if j == 0 or i == j:
#                 temp.append(1)
#             else:
#                 temp.append(P[i - 1][j] + P[i - 1][j - 1])
#         P.append(temp)
#     for i in P:
#         print(*i)  # *로 리스트 안의 내용만 출력 가능

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    dp = [[1]*i for i in range(N)]
    #1로만 채운 이차원 배열
    #파스칼 삼각형의 점화식
    #점화식 : dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    for i in range(2,N):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    print('#{tc}')
    for i in range(N):
        #for j in range(i):
        #print(dp[i][j],end='')
        print(*dp[i][0:i])