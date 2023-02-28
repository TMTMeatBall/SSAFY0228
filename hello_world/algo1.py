import sys

sys.stdin = open('./test.txt', encoding='UTF-8')

T = int(input())

for tc in range(1, T + 1):
    result = 0
    N, M = map(int, input().split()) # 밭의 행과 열
    matrix = [list(map(int, input().split())) for _ in range(N)] # 매트릭스

    total_cost = 0 # 나무를 심는 총 비용 계산
    cnt = 0 # 나무를 심는 수 계산
    exp = 0 # 가장 비싼 나무 계산
    col = 0 # 가장 비싼 나무가 심긴 열 계산

    for j in range(M): # 열을 기준으로 계산
        for i in range(N): # 행을 움직임
            if j % 2 == 0: # 가장 왼쪽 세로줄부터 심기 때문에 짝수열(0,2,4,...,)만 계산하면 된다.

                total_cost += matrix[i][j]  # 나무가 심기는 비용을을 각각 더해줌
                cnt += 1  # 나무가 심길때마다 + 1을 진행
                if exp < matrix[i][j]:     # 가장 비싼나무가 갱신될 때마다
                    exp = matrix[i][j]     # exp 값을 변환시켜줌
                    col = j                # j 는 단조증가하기 때문에,
                                           # 가격이 같은 비싼나무가 나왔을 때 업데이트 진행시켜주면 됨
    print(f'#{tc} ', total_cost, cnt, exp, col+1) # result 출력

