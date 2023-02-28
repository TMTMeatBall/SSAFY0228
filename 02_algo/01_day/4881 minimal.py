def dfstrack(i, N, s, visited):
    global minimalsum

    if i == N:
        if s < minimalsum:
            minimalsum = s
    elif s > minimalsum: #백트래킹을 성립하게 해주는 minimalsum 순회를 막는 효율적 코드
        return

    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = True
                dfstrack(i + 1, N, s + arr[i][j], visited)
                visited[j] = False


# 재귀함수의 핵심은 복구

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minimalsum = 9999999
    visited = [False] * N

    print(f'#{tc}', end=' ')
    dfstrack(0, N, 0, visited)
    print(minimalsum)
