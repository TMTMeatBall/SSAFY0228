# 첫 줄에는 테케 그 다음 줄부터 각 테케가 n개의 줄, 첫 줄에는 n이 다음 줄에는 2차원배열의 각 행이 n^2로
# 전체 지도 중 집 기지국 종류, 빈칸의 판별
# 기지국별로 커버되는 집 체크
# 커버되지 않은 집 확인
# 아이디어대로 작성
# 띄워쓰기가 없다 -> 그냥 input()으로 읽는다
# 공백을 포함하고 있다 -> input().split()을 사용
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    map = [list(input()) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            if map[i][j] != 'X' and map[i][j] != 'H':#기지국을 말함
                for k in range(1, ord(map[i][j]) - ord('A') + 2):
                    if i + k<N and map[i+k][j] == 'H':
                        map[i+k][j] = 'X'
                    if j+k<N and map[i][j+k]=='H':
                        map[i]
                    if i -k>-1 and map[i-k][j] ==
                    if j -k>-1 and map[i][j-k] ==
    for i in range(N):
        for j in range(N):
            if map[i][j] =='H':
                result +=1


    print(f'#{} {}'.format(tc,result))
