# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#
# 출력:
# -1-2-3-4-5-7-6
# bfs
# # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# N = 7
# E = 8
# adj = [[] for _ in range(N + 1)]
#
# # 인접 리스트 (노드끼리 서로 연결된 노드들을 표시)
# arr = list(map(int, input().split()))
# for i in range(E):
#     a = arr[i * 2]
#     b = arr[i * 2 + 1]
#     adj[a].append(b)
#     adj[b].append(a)
#
#
# # BFS
# def bfs(start):
#     # BFS, 큐
#     queue = []
#     # 방문 체크
#     visited = [False for _ in range(N + 1)]
#     queue.append(start)
#     visited[start] = True
#
#     # 반복을 진행하는데... 큐가 빌때까지
#     while queue:
#         node = queue.pop(0)
#         # node 탐색하는 추가 로직...
#         # ....
#         print(f'-{node}', end='')
#         for nxt_node in adj[node]:
#             if visited[nxt_node] == False:
#                 queue.append(nxt_node)
#                 visited[nxt_node] = True
#
#
# bfs(1)
# # 출력:
# # -1-2-3-4-5-7-6
# def dfs(graph, visited, start, end):
#     # 현재 위치가 목적지면 1 반환, 종료 (기저조건)
#     if start == end:
#         return True
#
#     # 현재 위치 방문 체크
#     visited[start] = True
#
#     # 현재 위치와 연결된 모든 노드 탐색
#     for nxt in graph[start]:
#         # 연결된 노드의 방문 여부 확인
#         if visited[nxt] == False:
#             # 들어갈 노드 방문 체크 해주고 재귀 호출
#             visited[nxt] = True
#             r = dfs(graph, visited, nxt, end)
#             # 목적지에 도달해서 반환받은 1로 종료
#             if r == True:
#                 return True
#
#     return False
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     # 정점 갯수와 간선의 갯수 입력
#     V, E = map(int, input().split())
#
#     # 인접 리스트를 생성하는데...
#     graph = [[] for _ in range(V + 1)]
#     for i in range(E):
#         s, e = map(int, input().split())
#         graph[s].append(e) # 단방향 그래프라서 s -> e
#
#     # S -> ... -> G 연결하는 경로가 있는가...?
#     S, G = map(int, input().split())
#
#     # 방문 체크할 배열 생성
#     visited = [False] * (V + 1)
#
#     # 목적지 도달했는지 여부로 결과 출력
#     result = dfs(graph, visited, S, G)
#     if result == True:
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
N = 7
E = 8
adj = [[] for _ in range(N + 1)]
arr = list(map(int, input().split()))
for i in range(E):
    a = arr[i * 2]
    b = arr[i * 2 + 1]
    adj[a].append(b)
    adj[b].append(a)


# # 인접 리스트(노드끼리 서로 연결된 노드들을 표시)
# def dfs(visited, start):
#     # 기저조건(종료를 하는 지점)
#     if visited[start] == True:
#         return
#     # 해당 노드를 방문하였음
#     visited[start] = True
#     print(f'-{start}', end='')
#
#     # 해당 노드에서 다른 노드의 정점으로 이동하는 코드를 작성필요
#     for nxt_node in adj[start]:
#     # 값 추가 코드
#     # ...
#     dfs(visited, nxt_node)
#     # 값을 복원하는 코드
#     # ...
#
#
# visited = [False for _ in range(N + 1)]
# dfs(visited, 1)

def bfs(start):
    queue =[]
    visited = [False for _ in range(N+1)]
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.pop(0)
        print(f'-{node}', end='')
        for nxt_node in adj[node]:
            if visited[nxt_node] == False:
                queue.append(nxt_node)
                visited[nxt_node] = True

bfs(1)