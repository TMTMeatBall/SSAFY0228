T = int(input())
for tc in range(1,T+1):
    N = str(input())
    result = 1 if N[:] ==N[::-1] else 0

    print(f'#{tc} {result}')