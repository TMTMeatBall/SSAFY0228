T = int(input())
for tc in range(1,T+1):
    N,K,A,B = map(int,input().split()) #N = 하늘 #K = 사진의 초점이 잡는 크기 #(A,B) = 초점의 좌표

    arr = [list(input().split()) for _ in range(N)] #array 받기
    print(arr)

    arr[A][B] #초점 크기?

    #점점 K사각형을 (-1,-1,-1,-1)씩 줄여 나가는데, 그렇게 만들어지는 사각형의 최 외각에 별이 하나라도 걸리면 종료해야 함.
    #또는 첫 k사각형이 그려졌을 떄에, 모든 별이 그 안에 없다면, -1을 반환하게 해야 함
    K = 9 (4,5) 에서
    실제 범위로 갖는 값은 (0,1) (8,9)
    A +- K//2
    B +- K//2
    arrK
    #사각형이 큰 사각형 바깥으로 나가지 않게
    for i in range(A-K//2):
        for j in range(B-K//2):
