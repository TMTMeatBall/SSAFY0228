def f(i):
    if i>0:
        f(left[i])
        print(data[i],end='')
        f(right[i])


T = 10
for tc in range(1, T+1):
    N = int(input())
    left = [0]*(N+1)
    right = [0]*(N+1)
    data = [0]*(N+1)
    for _ in range(N):
        arr = list(input().split())
        p = int(arr[0])
        ch = arr[1]
        data[p] = ch
        if len(arr) == 4:
            left[p] = int(arr[2])
            right[p] = int(arr[])