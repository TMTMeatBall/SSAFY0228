T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    #[list(map(int, input().split())) for _ in range(N)]과의 차이가 무엇인가? 이거 대답할 수 있어야 함
    farms = 0
    a = N // 2
    b = N // 2
    for i in range(N):
        for j in range(a, b+1):
            farms += arr[i][j]

        if i < N // 2:
            a -= 1
            b += 1
        else:
            a += 1
            b -= 1

    print(f'#{tc} {farms}')
# # # 1. 홀수개로 늘어나는 마름모 별찍기
# split() 메서드를 쓰는 법 새로 알기
# 이차원배열 선언 다시 해보기
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     a = [list(map(int, input())) for _ in range(N)]
#     ans = 0  # output 변수
#
#     # s: 시작포인트, e: 끝포인트
#     s, e = N // 2, N // 2
#     for i in range(N):
#         for j in range(s, e + 1):
#             ans += a[i][j]
#         # 행의 인덱스가 mid 전까지는 s-e 간격 늘리고 mid 이후로는 간격 줄임
#         if i < N // 2:
#             s -= 1
#             e += 1
#         else:
#             s += 1
#             e -= 1
#
#     print("#{} {}".format(tc, ans))