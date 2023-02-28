#달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이뤄져 있다.
#달팽이의 크기 N은 1이상 10이하의 정수
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

#가장 첫 줄에는 테스트 케이스의 개수 T
T = int(input())
for tc in range(1,T+1):
    #각 테스트 케이스에는 N이 주어진다.
    #각 줄은 '#tc'로 시작, 다음 줄부터 빈칸을 두고 달팽이 숫자를 출력
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    r, c = 0,0 #좌표
    dist = 0 #회전방향 0:동 1:남 2:서 3:북

    for n in range(1, N*N +1):
        snail[r][c] =n
        r += dr[dist]
        c += dc[dist]

        if r< 0 or c<0 or r>=N or c>= N or snail[r][c] !=0:
            r -= dr[dist]
            c -= dc[dist]
            dist = (dist+1)%4
            r += dr[dist]
            c += dc[dist]

    print('#{}'.format(tc))
    for row in snail:
        print(*row)
    print()