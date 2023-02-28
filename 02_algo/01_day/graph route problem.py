# #1. 그래프 - 인접행렬로 작성하는 방법
# node, edge = map(int, input().split())
# # 노드의 갯수가 N이고 N*N의 이차원 배열을 만든다.
#a-> f 연결되어 있는지 확인해라 adj[a][f]
#a-> ? 연결되어 있는지 모두 확인해라 for x: 0-> node -1
                                    #if adj[a][x] ==1:
#정점과 가중영역
# adj = [[0 for _ in range(node)]for _ in range(node)]
# #입력으로 노드간의 연결을 입력으로 받는다(간선 정보)
# for _ in range(edge):
#     src, dest = map(int,input().split())#시작정점과 끝 도착점을 입력
#     adj[src][dest] = 1 #src-> dest 서로 연결점이 존재
#     adj[dest][src] = 1 #거꾸로 하면 dest -> src의 양방향 연결점이 존재

#2. 그래프 - 인접리스트로 작성하는 방법(연결 관계만 기록하는 방법)
# a-> [b, c, f] / b-> [a, f]
node, edge = map(int, input().split())
#노드의 갯수 만큼 빈 리스트를 작성
adj = [[0 for _ in range(node)] for _ in range(node)]
src, dest = map(int,input().split())
for _ in range(edge):
    src, dest = map(int,input().split())
    adj[src].append(dest) = 1
    adj[dest].append(src) = 1


#1. 0으로 된 리스트를 만들어서 인덱스(그래프 모양) 파악
#2. 방문함, 