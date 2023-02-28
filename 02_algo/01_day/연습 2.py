T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = input()

    stack = []
    result = 1

    for i in range(N):
        if arr[i] == '(' or arr[i] == '{' or arr[i] == '[' or arr[i] == '<':
            stack.append(arr[i])
        if arr[i] == ')':
            if len(stack) >0 and stack.pop() != '(':
                result = 0
                break
        # 이하 4개
    print(+)