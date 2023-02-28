# 1. DFS
def dfs(graph, start):
    visited = []
    stack = []
    stack.append(start)
    while stack:  # 스택 안에 뭐라도 있으면,
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    print('dfs', visited)
    return visited

    a = int(input())
    dfs(a, '1')


# 2. BFS
N = 7
E = 8
adj = [[] for _ in range(N + 1)]
arr = list(map(int, input().split()))
for i in range(E):
    a = arr[i * 2]
    b = arr[i * 2 + 1] #쌍방향으로 연결되어 있는가? 를 알기 위해>? 있는>? 뭐 그런?
    adj[a].append(b)
    adj[b].append(a)


def bfs(start):
    queue = []
    visited = [False for _ in range(N + 1)]
    queue.append(start)
    visited[start] = True
    # queue가 빌 때까지 반복
    while queue:
        node = queue.pop(0)
        # node 탐색을 위한 추가 로직을 여기에 추가
        # ...
        print(f'-{node}', end='')
        for nxt_node in adj[node]:
            if visited[nxt_node] == False:
                queue.append(nxt_node)
