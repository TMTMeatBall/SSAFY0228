T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    # 가장 처음에는 N개의 상자가 모두 0으로 쓰여진 상태
    result = [0] * (N + 1)

    for i in range(Q):
        left, right = map(int, input().split())
    for j in range(left, right + 1):
        result[j] = i

    print(f'#{tc}', end='')
    print(*result[1:])
