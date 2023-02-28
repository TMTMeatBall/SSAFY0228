T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split)

    graph = [[] for _ in range(v+1)]
    for i in range(e):
        s,e = map(int,input().split())
        graph[s].append(e)
    s, g = map(int,input().split())
    visit = [False]* (v+1)
    result = func(s,g)
    if result == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


def dfs(graph,visited,start,end):
    if start == end