T = int(input())
for tc in range(1, T + 1):
    N, K, A, B = map(int, input().split())

    sky = [list(input().split()) for _ in range(N)]

    # 확대수
    result = 0
    # camera = [sky[i][A - (K // 2):A + (K // 2)] for i in range(B - (K // 2), B + (K // 2))]
    camera = [[0] * K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            camera[i][j] = sky[A - (K // 2) + i][B - (K // 2) + j]
    star_camera = sum(a.count('*') for a in camera)
    star_sky = sum(b.count('*') for b in sky)

    if star_sky != star_camera:
        print(f'#{tc} -1')
    # else:
    while star_sky == star_camera:
        for i in range(A):
            for j in range(B):



    print(f'#{tc} {result}')
    #     while not star_camera < star_sky:
    #         if star_camera == star_sky:
    #             K -= 2
    #             result += 1
    #
    # print(f'#{tc} {result}')
    #     break
    # while not star_camera < star_sky:
    #     if star_camera == star_sky:
    #         K -= 2
    #         result += 1
    #         break
    if new_stars != origin_stars:

    while new_stars == origin_stars:
        k-= -1
        new_stars = 0
        for i in range(A-k,a+k+1):
            for j in range(B-k,b+k+1):
                if 0<=1<N and 0<=j<N and mapp[i][j]=='*'
                    new_stars += 1
        if new stars == origin
        cnt +=1

    # 결국 두 범위 안에서 별 갯수가 다르면 처음부터 다다를 수 없었으므로 -1 반환

    # 요점은, 스카이 스타와 카메라 스타가 같다면, K-2씩 해가고, 달라진 시점에서 break하고 result
    # result 에 반환

    # for i in camera
    #     a.append('*')
    # print(camera)
    # print(a)
    # star_count = a.count('*')
    # print(star_count)
    #     if camera == 0:
    #         break
    #     if camera != K * K:
    #         result = -1
    #         break
    #     if K == 1:
    #         break
    #
    #     K -= 2
    #     A += 1
    #     B += 1
    #     count += 1
    #
    # print(f'#{tc} {count}')
