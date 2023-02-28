def bfs(S, G): #start 노드부터 Goal노드까지 간선 수를 반환
    #다음 노드로 건너갈 때마다 cnt+=1

    visited = [False for _ in range(V + 1)]
    result = [0 for _ in range(V + 1)]
    queue = []
    queue.append(S)
    visited[S] = True
    result[S] = 0
    while queue: #완전 탐색이 되도록
        # S=1에서 인접adj 3,4를 받지 못하고 있다
        node = queue.pop(0)
        for nxt_node in adj[node]:
            if visited[nxt_node] == False:
                queue.append(nxt_node)
                visited[nxt_node] = True
                result[nxt_node] = result[node] + 1
    return result[G]


# G를 못 쓰고 있음
# 최소 몇 개의 간선을 지나는 가를 셀 수 있어야 함


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # Node & Edge
    # 간선 노드 번호

    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())  # Start & Goal
    adj = [[] for _ in range(V + 1)]  # 노드 갯수만큼 만들되 +1개 만드는 이유는
    # 노드는 1부터 시작하는데 리스트 인덱싱은 0부터 시작하므로, 맞추기 위해서 +1개로 만들고
    # adj[0]을 버린다.
    print(arr)
    print(adj)
    for i in range(E):
        a = arr[i][0]
        b = arr[i][1]

        adj[a].append(b)
        adj[b].append(a)

    result = bfs(S, G)

    print(f'#{tc} {result}')
