def count_stars(sky, i, j, K):
    """
    sky: 전체 하늘 정보가 담긴 2차원 리스트
    i, j: 현재 위치
    K: 카메라 크기

    현재 위치에서 K x K 범위 내에 있는 별의 개수를 반환하는 함수
    """
    star_cnt = 0
    for r in range(i - K // 2, i + K // 2 + 1):
        for c in range(j - K // 2, j + K // 2 + 1):
            if 0 <= r < len(sky) and 0 <= c < len(sky[0]):
                if sky[r][c] == '*':
                    star_cnt += 1
    return star_cnt


T = int(input())
for tc in range(1, T + 1):
    N, K, A, B = map(int, input().split())
    sky = [input().rstrip() for _ in range(N)]
    result = -1

    # 현재 위치에서 K x K 범위 내에 있는 별의 개수 계산
    star_cnt = count_stars(sky, A, B, K)

    # 현재 위치에서 K x K 범위 내에 있는 별의 개수가 전체 별의 개수보다 작은 경우
    if star_cnt < sky.count('*'):
        # K를 줄여가며 별의 개수가 전체 별의 개수 이상이 될 때까지 반복
        while K > 1:
            K -= 2
            new_star_cnt = count_stars(sky, A, B, K)
            if new_star_cnt >= sky.count('*'):
                result = tc
                break
    else:
        result = tc

    print(f'#{result} {K}')