
def dfs(s,g):
    stack = []#이건 리스트가 아니라 스택이다(다른 언어에서는 엄연히 다르다) #스택 지정
    stack.append(s) #스택에 스타트지점을 append
    while stack :
        a = stack.pop() #stack 에서 pop을 했을 때에, 값이 있다면
        visited[a] = 1 #visited는 [a]지점에서 1(방문함)값을 받는다

        for i in range(len(adj[a])):
            if visited[adj[a][i]] == 0:
                if adj[a][i] == g:
                    return 1
            stack.append(adj[a][i]) #갈 수 있는 지점을 stack에 append함 return이 1이 아닌 경우에
    return 0


T = int(input()) #testcase
for tc in range(1, T+1):
    v, e = map(int,input().split()) # 노드와 간선의 갯수
    visited = [0 for _ in range(v+1)] # 이것이 0일때 방문하지 않은 것, 1로 채워지면 방문한 것으로 취급
    adj = [[] for _ in range(v+1)] #

    for _ in range(e):#이후 제공되는 간선 갯수 e수만큼을 받아야 함
        i, j = map(int, input().split())
        adj[i].append(j) #방향성 그래프이므로 양방향이 아니므로 i->j만을 따짐
        # adj[j].append(i)

    s,g = map(int,input().split()) #start and goal

    print(f'#{tc} {dfs(s,g)}')

