T = int(input())
for tc in range(1, T + 1):
    N, K, A, B = map(int, input().split())

    sky = [list(input().split()) for _ in range(N)]

    result = 0

        # 현재 위치에서 확대한 카메라 범위 계산
    camera = [[sky[i][j] for j in range(B - K//2, B + K//2+1)] for i in range(A - K//2, A + K//2+1)]

    # 카메라로 촬영한 별 개수 계산
    star_camera = sum(row.count('*') for row in camera)

    # 전체 하늘에서 별 개수 계산
    star_sky = sum(row.count('*') for row in sky)
    if star_camera < star_sky: # 현재 별 개수가 원래 별 개수보다 작을 경우 -1 반환
        result = -1
    while True:

        # 현재 별 개수와 원래 별 개수가 같으면서 K를 줄여나갈 경우
        if star_camera == star_sky:
            K -= 2
            result += 1
        else:
            break

    print(f'#{tc} {result}')