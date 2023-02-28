def 색칠(dy,dx,color,cube):
    cube[dy][dx]
    dy=[1,1,1,0,-1,-1,-1,0]
    dx=[-1,0,1,1,1,0,-1,-1]


    T = int(input())
    for tc in range(1+T+1):
        n = int(input())
        room = [0]*200
        for _ in range(n):
            a,b = map(int,input().split())
            a=-1
            b=-1
            a //=2
            b//=2
            if a>b:
                a,b = b,a
            for i in range(a,b+1):
                room[i] += 1
                print(f'#{tc} {max(room)}')

