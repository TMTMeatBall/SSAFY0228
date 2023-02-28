T= int(input())
for tc in range(1,T+1):
    #거리, A열차 속력,B열차 속력,파리속력
    D,A,B,F = list(map(int,input().split()))

    print(f'#{tc} {(D/(A+B))*F}')
    