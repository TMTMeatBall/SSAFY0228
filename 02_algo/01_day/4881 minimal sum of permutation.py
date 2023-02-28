def f(i, N):
    if i == N:  # 기저조건 i가 N에 닿았으므로 끝내는 조건
        print(A)
        # 기저조건(순열이 끝나는 곳) 에서 나머지 값 비교코드를 적는다.

        return
    for j in range(i, N):
        A[i], A[j] = A[j], A[i]
        f(i + 1, N)
        A[i], A[j] = A[j], A[i]


T = int(input())
for tc in range(1, T + 1):
    k = int(input())  # k는 k*k배열을 의미하는 인풋
    A = []  # A를 이차원배열로
    for i in range(k):
        A.append(list(map(int, input().split())))
    # int(input)을 받아서 1부터 N까지를 요소로 리스트를 뽑기?
    N = len(A[i])
    print(f'#{tc} {f(0,N)}')




# #1. 이차원배열로 입력받고 1개 잡고 행 순으로 서로 비교해서 최소값만을 더하면 되지 않나?
# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(list(map(int,input().split())))
#
# #2. 각 행을 뽑아내면서 안의 요소를 쓱 돌면서 최소값을 하나씩 뽑아서 그냥 result 에 += 한다
# result = 0
# min = 99
# for i in range(N):
#     for j in range(N):
#         arr[]
#
#
# print(f'#{tc} {arr}')
# 이렇게 받으면 두 번째 조건인 같은 세로줄에서 2개 이상 뽑아서는 안된다는 규칙을 어기게 된다.
