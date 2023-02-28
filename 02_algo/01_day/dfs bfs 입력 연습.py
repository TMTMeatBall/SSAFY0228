def dfs(graph,start):
    visited =[]
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited

def bfs(graph,start):
    visited = []#visited
    queue = []#queue
    queue.append(start)#start -> queue
    while queue: #if len(queue) !=0:
        next_node = queue.pop(0)
        if next_node not in visited:
            visited.append(next_node)
            queue.extend(graph[next_node])
    return visited


def bfs(graph,start):
    visited = []
    queue = []

    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])#이 그래프[노드]는 인접한 모든 점들을 queue에 extend 하는 기능을 갖는다

    return visited

def dfs(graph, start):
    visited = []
    stack =[]
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.expend(graph[node])
    return visited

# 인접에 대해서 쓸 수 있어야 함

