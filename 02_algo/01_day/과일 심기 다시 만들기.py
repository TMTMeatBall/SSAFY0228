T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fruits = []
    fruits_col = []
    for i in range(N):
        for j in range(0, M, 2):
            fruits.append(arr[i][j])
    for i in range(N):
        for j in range(0, M, 2):
            if arr[i][j] == max(fruits):
                fruits_col.append(j)
    fruits_col.sort()

    print(f'#{tc} {sum(fruits)} {len(fruits)} {max(fruits)} {fruits_col[-1] + 1}')
