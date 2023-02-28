T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    words = [input() for _ in range(N)]
    cnt = 0
    firstwords = []
    for i in words:
        firstwords.append(i[0])
    firstwords.sort()
    a = []
    for i in firstwords:
        if i not in a:
            a.append(i)

    # 연속되는 알파벳인지 체크하는 방법?
    cnt = 0

    if a[0] == 'A':
        cnt += 1
        if a[1] == 'B':
            cnt += 1
            if a[2] == 'C':
                cnt += 1
                if a[3] == 'D':
                    cnt += 1
                    if a[4] == 'E':
                        cnt += 1
                        if a[5] == 'F':
                            cnt += 1
                            if a[6] == 'G':
                                cnt += 1
                                if a[7] == 'H':
                                    cnt += 1
                                    if a[8] == 'I':
                                        cnt += 1
                                        if a[9] == 'J':
                                            cnt += 1
                                            if a[10] == 'K':
                                                cnt += 1
                                                if a[11] == 'L':
                                                    cnt += 1
                                                    if a[12] == 'M':
                                                        cnt += 1
                                                        if a[13] == 'N':
                                                            cnt += 1
                                                            if a[14] == 'O':
                                                                cnt += 1
                                                                if a[15] == 'P':
                                                                    cnt += 1
                                                                    if a[16] == 'Q':
                                                                        cnt += 1
                                                                        if a[17] == 'R':
                                                                            cnt += 1
                                                                            if a[18] == 'S':
                                                                                cnt += 1
                                                                                if a[19] == 'T':
                                                                                    cnt += 1
                                                                                    if a[20] == 'U':
                                                                                        cnt += 1
                                                                                        if a[21] == 'V':
                                                                                            cnt += 1
                                                                                            if a[22] == 'W':
                                                                                                cnt += 1
                                                                                                if a[23] == 'X':
                                                                                                    cnt += 1
                                                                                                    if a[24] == 'Y':
                                                                                                        cnt += 1
                                                                                                        if a[25] == 'Z':
                                                                                                            cnt += 1

    print(f'#{tc} {cnt}')

    # b = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') #2. abcd...z 리스트를 만들어서 i 가 이 리스트를 순회하면서 a리스트와 비교하고,
    #같으면 cnt+= 1 하는 것으로 한다
    # b = ['A', 'B', ...] #위와 동일하지만, 안의 요소를 전부 분해했음
    # b = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    # cnt = 0
    # for idx in range(len(a)):
    #     if a[idx] == b[idx]:
    #         cnt += 1
    #
    # print(f'#{tc} {cnt}')
