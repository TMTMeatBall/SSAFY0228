def inorder(t):
    if t <= N:
        inorder(t * 2)#좌측
        print(tree[t], end='')#자기자신
        inorder(t * 2 + 1) #우측


T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        a = input().split()
        word = a[1]
        tree[i] = word
    print(f'#{tc} ', end='')
    inorder(1)
    print()
