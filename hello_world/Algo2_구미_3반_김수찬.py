def fnd_stars(matrix, n):  # 별을 찾는 함수
    s = list()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '*':
                s.append([i, j])
    return s


def camera(items, a, b, k):  # 별과 초점, 영역의 크기를 주어주면, 그 사이 범위에서 별을 찾겠다.
    l = k // 2               # zoom 할 때 발생하는 간격의 최댓값
    target = len(items)      # 별의 총 갯수
    rlt = 0                  # 출력될 변수
    is_first = True          # 첫번째 사진에 대한 Flag

    # 0번 Zoom 부터 최대 가능한 zoom 까지
    for i in range(l):
        zoom = l - i

        # 간격의 범위를 지정
        lx = a - zoom if a - zoom >= 0 else 0
        ly = b - zoom if b - zoom >= 0 else 0
        rx = a + zoom if a + zoom < N else N
        ry = b + zoom if b + zoom < N else N

        cnt = 0  # 별들의 수를 counting 하는 변수
        for item in items:  # 원하는 영역 안에 있는 별들인지 조사.
            if lx <= item[0] <= rx and ly <= item[1] <= ry:
                cnt += 1

        if cnt == target:  # zoom in 을 했을 때, 별들이 영역 안에 모두 들어가 있다면
            is_first = False
            rlt = i  # 초점을 확대해도 상관이 없다.
        elif (cnt < target) and (not is_first):  # zoom in을 했을 때 별들이 몇개 안보일경우
            rlt = i - 1  # 이전의 결과가 최대로 zoom in 할 수 있는 수이다.
            break
        elif is_first:  # 첫번째 사진인데 별이 영역에 들어가있지 않다면, result = -1 출력
            rlt = -1
            break

    return rlt  # 결과로 나온 확대 횟수를 출력


T = int(input())
for tc in range(1, T + 1):
    N, K, A, B = map(int, input().split())
    sky = [list(input().split()) for _ in range(N)]

    stars = fnd_stars(sky, N)        # 별들을 찾는다.
    result = camera(stars, A, B, K)  # 몇번 zoom 했는지 확인해본다.

    print(f'#{tc} ', result)         # result 출력