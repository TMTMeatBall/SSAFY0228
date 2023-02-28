#10개의 테스트케이스
#각 테스트케이스마다 첫 줄에는 N (1 <= N <= 100)
#두 번째 줄부터는 N줄에 걸쳐 NxN개의 정수가 입력됨, 정수들은 공백으로 구분되어 입력된다.
#상하좌우로 이웃한 요소와의 차이
import sys
sys.stdin=open('1in.txt','r')

board = [list(map(int,input().split()) for _ in range(n))]
total = 0 #총합을 넣을 변수
dx = [-1,1,0,0]
dy = [0,0,-1,+1]
#dx dy가 보드 바깥으로 나가지 않게 하는 처리
for i in range(n):
    for j in range(n):
        hap = 0
        if 0 <= i -1 < n and 0 <= j < n:
            total += abs(board[i][j] -board[i-1][j])
        if 0 <= i +1 and 0 <= j <n:
            total += abs(board[i][j] - board[i+1][j])

        if 0 <= i and 0 <= j-1 < n:
            total += abs(board[i][j] - board[i][j-1])
        if 0 <= i and 0 <= j+1 < n:
            total += abs(board[i][j] - board[i][j+1])
        #board[i][j]
    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]
        if 0 <= x<n and 0 <= y <n:
            #board[x][y]
             total += abs(board[i][j] - board[x][y])
        total += hap
    print(f'{tc} {total}')