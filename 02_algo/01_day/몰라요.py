T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    field = []

    for n in range(N):
        arr = list(map(int, input().split()))
        field.append(arr)
    sum = 0
    count = 0
    max_f = field[0][0]
    max_f_low = 0

    for j in range(0, M, 2):
        for i in range(0, N):
            count += 1
            sum += field[i][j]
            if field[i][j] >= max_f:
                max_f = field[i][j]
                max_f_low = j + 1

    print(f'#{tc} {sum} {count} {max_f} {max_f_low}')
