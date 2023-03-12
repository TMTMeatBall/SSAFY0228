T = int(input())
for tc in range(1, T + 1):
    number = int(input())
    saved = []
    cnt = 0
    result = 0
    times = 1
    while len(saved) < 9:
        k = str(number * times)
        k = list(k.split())
        k.sort()
        times += 1
        cnt += 1
        for i in range(len(k)):

            if k[i] in saved:
                pass
            else:
                saved.append(k[i])
                saved.sort()

    # 계산한 값을 분해해서 그 내용물이 saved에 없다면,

    if len(saved) == 10:
        result = cnt

    print(f'#{tc} {result}')
