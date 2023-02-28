T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    poss = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            candi = 0
            a = numbers[i] * numbers[j]
            candi += a
            b = str(candi)
            for k in range(len(b) - 1):
                # if b[k] <= b[k + 1]:  ###
                #     continue  ###
                # else:  ###
                #     break  ###
                if b[k] > b[k + 1]: #for-else를 통해 if가 for-k에서 모든 경우에 참을 반환할 때에, else로 넘어가서 append 하도록 만들기
                     break
            else:
                poss.append(a)
    if len(poss) == 0: #poss의 전체 요소 갯수가 0인 경우에 -1을 뱉는 조건을 설정
        print(f'#{tc} -1')
    else:
        poss.sort()
        result = poss[-1]
        print(f'#{tc} {result}')
