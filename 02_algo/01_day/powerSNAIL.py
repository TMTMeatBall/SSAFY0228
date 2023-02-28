t = int(input())

for a in range(1,t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    num = 0
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    directionidx = 0
    curX, curY = 0, -1 #current 위치
    while num < n*n : #숫자는 총 사각형이 갖는 넓이 이상을 가질 수 없다
        tmpX = curX + direction[directionidx][0] #처음 direX는 0을 갖다가 다음에는 1,2,3으로 변하면서
        tmpY = curY + direction[directionidx][1] #다른 값을 갖게 한다
        #tmpX,tmpY는 direction을 뱅글뱅글 돌리게 하는 행렬 이동방향을 결정하게 한다.
        #범위 초과시 방향을 바꾼다
        if tmpX < 0 or tmpY < 0 or tmpX >= n or tmpY >= n or arr[tmpX][tmpY] != 0:

            #tmpX tmpY가 0보다 작은 경우는  또는 tmpX,tmpY가 n보다 큰 경우는 사각형을 넘어갔을 때
            #arr의 tmpX,tmpY좌표가 0이 아닌 때
            directionidx += 1 #하는 것으로 참조direction list에서의 참조 인자가 바뀐다.

            if directionidx == 4:#directionx는 최대가 3이므로, 0123 4가 된 경우엔
                directionidx = 0 #0으로 다시 바꿔서 list direction=[]을 돌게 한다.
        else:
            num += 1 #directionx가 0123에 위치한 경우, num을 합산하면서 칸에 숫자를 넣는다.
            curX, curY = tmpX, tmpY#curX,curY는 tmpX, tmpY의 객체로 갱신되면서 점차 커진다.
            arr[curX][curY] = num
    print(f'#{a}')#결과창의 testcase에 대해서 신경 좀 쓰기
    for row in arr:
        print(*row)
    #print("#%d" % (a+1))
    # for row in arr:
    #     print(' '.join(map(str, row)))