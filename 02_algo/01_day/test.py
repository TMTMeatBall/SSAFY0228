T = int(input())

for n in range(1, T + 1):
    N = int(input())
    a = list(map(int, input()))

    lst = [0] * 10
    for i in a:
        lst[i] += 1

    mx = 0
    idx = 0

    for k in range(9, -1, -1):
        if lst[k] > mx:
            mx = lst[k]
            idx = k

    print(f'#{n} {idx} {mx}')