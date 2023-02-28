#10x10 격자에 빨/파를 칠한다
#N개영역에 대한 왼쪽위, 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어진 떄에
#색이 겹쳐 보라색이 된 칸수를 구하는 프로그램 작성
#2
#2 2 4 4 1
#3 3 6 6 2
#첫 줄엔 테스트 케이스 갯수 T
T = int(input())
for tc in range(1,T+1):
    #10x10 틀 만들기
    board = [[0 for j in range(10)] for i in range(10)]#i가 가로 j가 세로
    #다음 줄부터 테스트 케이스의 첫 줄에 칠할 영역의 갯수 N이 주어진다
    N = int(input())
    for n in range(N):
        result=0
        #왼쪽 인덱스 r1, c1, 오른쪽 아래 인덱스 r2, c2 색상정보 color(0 ≤ r1, c1, r2, c2 ≤ 9 )
        r1,c1,r2,c2,color = list(map(int,input().split())) #
        for r in range(r1,r2+1): #2~4까지 #또는 3~6까지
            for c in range(c1,c2+1): #2~4까지 #또는 3~6까지
                if color == 1: #붉은색일때
                    board[r][c] +=1 #board 10x10을 만드는 이유1
                if color == 2: #푸른색일 때
                    board[r][c] +=1 #board 10x10을 만드는 이유2
    for i in board:#board 10x10을 만드는 이유3 board에서 color에 따라 모든 칸에 012세 값중 하나가 지정되었다
        for j in i: #좌표계 i행 j열 에서
            if j == 2: #죄표값이 2인 좌표를 찾으면,
                result += 1 #result 에 1을 합함

    print(f'#{tc} {result}')