def op(oper, a, b):
    if oper == '-':
        return a - b
    if oper == '+':
        return a + b
    if oper == '*':
        return a * b
    if oper == '/':
        return a / b


def postorder(node):
    if type(tree[node]) == int:
        return tree[node]
    # 좌-우-자기자신

    # left
    a = postorder(node * 2)
    # right
    b = postorder(node * 2 + 1)
    # 자기 자신
    c = op(postorder)

    # 기저 조건(종료조건)이 필요
    # 피연산자, 숫자가 나오면 반환


T = 10
for tc in range(1, T + 1):
    N = int(input())
    # 정점이 정수면 정점 번호와 양의 정수가 주어지며,
    # 정점이 연산자이면 정점 번호, 연산자, 해당 정점의 좌,우 자식 노드 번호가 제공됨
    # arr 를 받는 방법?
    # 후위 순회를 한다.
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for _ in range(N):
        tmp = input().split()
        if tmp[1].isdigit() == True:
            node, value = map(int, tmp)
        else:
            node, oper, l, r = tmp
            node, l, r = map(int, (node, l, r))
            tree[node] = oper
            left[node] = l
            right[node] = r
    result = postorder(1)
    print(f'#{tc} {result}')
