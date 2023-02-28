def op(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '/':
        return a // b
    else:
        return a * b

def post_order(node):
    if 0 < node <= N:
        if type(tree[node]) == int:
            return tree[node]
        a = post_order(dir[node][0])
        b = post_order(dir[node][1])
        return op(tree[node], a, b)

for tc in range(1, 11):
    N = int(input())

    tree = [0] * (N + 1)
    dir = [0] * (N + 1)

    for _ in range(N):
        tmp = input().split()
        if tmp[1].isdigit():
            node, value = map(int, tmp)
            tree[node] = value
        else:
            node, operator, l, r = tmp
            node, l, r = map(int, (node, l, r))
            tree[node] = operator
            dir[node] = [l, r]

    result = post_order(1)
    print(f'#{tc} {result}')