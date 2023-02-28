# def BFS(g, s): #그래프 g, 탐색 시작점 s
#     visited = [0] * (n + 1)  # 정점의 갯수+1큐의 특징만큼 0을 갖는 visited 리스트의 선언
#     queue = []#queue선언
#     queue.append(s)  # 시작점 삽입
#     while queue:  # queue가 비어있지 않음이 True 일때에,
#         t = queue.pop(0) #t가 가장 앞에 있고,
#         if not visited[t]:
#             visited[t] = True
#             visit(t)
#             for i in g[t]:
#                 if not visited[i]:
#                     queue.append(i)
# visited 생성-queue생성-시작점을 in queue 하는 작업이 기본
# 그리고 이하 과정을 반복시킴
def bfs(v, N):
    visited = [0] * (N + 1)  # visited 생성
    q = [v]  # -queue생성-시작점 in queue

    visited[v] = 1
    while q:  # queue가 비어있지 않을 때에,
        t = q.pop(0)
        print(t, end=' ')  # t에서 처리할 일
        for v in adjL[t]:  # t에 인접이면서 방문한 적 없는 v
            if visited[v] == 0:
                q.append(v)  # v 인큐
                visited[v] = visited[t] + 1  # v를 enqueue했음을 표시

    print()
    print(visited)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V + 1)]  # 인접 리스트
for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
print()
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 
'''
# bfs(v,n) -> bfs(i,j,n)
# visited를 이차원으로 제작?한다?
