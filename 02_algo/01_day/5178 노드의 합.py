def post_order(t):
    #후위 -> LRV

    if tree[t]:
        return tree[t]

    hap = 0
    hap += post_order(t*2)
    hap += post_order(t*2+1)
    tree[t] = hap





T = int(input())

for tc in range(1,T+1):
    N,M,L = map(int,input().split())

    tree = [0 for _ in range(N+1)]

    for _ in range(M):
        t, data = map(int,input().split())

post_order(1)
print(f'#{tc} {tree[L]}')
