def f(i,N):
    #기저조건 (i == N) 이 되었을 때에 종료
    if i == N: #순열 완성
        print(A)
        return
    #각 재귀호출마다 i를 배정하고

    #for j : i -> N-1 [i,N)
    for j in range(i,N):
        #배열요소를 교환하면서 다른 결과
        A[i], A[j] = A[j], A[i]
        #다음 단계로 진행
        f(i+1, N)
        #배열 요소 원상복구
        A[i], A[j] = A[j], A[i]

#시작되는 정점은 각 i=1,i=2,i=3,i=4라면 i=1에선 1부터 시작
#i=2부턴 2부터 시작...
#
A = [1,2,3]
N = len(A)
f(0,N)

def f(i, N):
    # 기저조건 (i == N) 종료해라...
    if i == N: #순열완성
        print(A)
        return

    # for j : i -> N-1 [i, N)
    for j in range(i, N):
        # 배열 요소 교환
        A[i], A[j] = A[j], A[i]
        # 다음 단계로 진행
        f(i + 1, N)
        # 배열 요소 원복
        A[i], A[j] = A[j], A[i]


A = [1,2,3]
N = len(A)
f(0, N)