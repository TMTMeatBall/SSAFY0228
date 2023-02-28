#트리의 정점의 총 수 V 간선은 V-1
#간선은 부모 정점 번호가 작은 것부터 나열됨
#V= 13
#1 2 1 3 2 4 3 5 3 6 4 7 58 5 9 6 10 6 11 7 12 11 13

#이상의 이진트리 표현에 대해서 전위 순회하여 정점번호를 출력
#조상루트 찾기
#정점 루트인덱스로 번호를 저장하는 것
def DFS(n):
    for i in tree[n]:
        if par[i] == -1:
            par[i] = n
            DFS(i)



V = 13
tree = [[] for _ in range(V+1)]
par = [-1]*(V-1)
for _ in range(V-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

DFS(1)
for i in range(2,V+1):
    print(par[i])