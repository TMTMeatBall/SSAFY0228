#N개의 정수가 주어지면, 가장 큰 수, 가장 작은 수, 두 번째로 큰 수, 두 번째로 작은 수
#첫 줄에 테스트 케이스T가 주어진다
T = int(input())
for tc in range(1,T+1):
    #다음 줄에 정수의 갯수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다.
    N = int(input())
    ai = list(map(int,input().split()))
    #특별히 정렬된 숫자는 총 10개를 출력한다.
    for i in range(10):
        if not i % 2:
            max_idx = i
            for j in range(i+1,N):
                if ai[max_idx] < ai[j]:
                    max_idx = j
            ai[i], ai[max_idx] = ai[max_idx], ai[i]
        else:
            min_idx = i
            for j in range(i+1,N):
                if ai[min_idx]>ai[j]:
                    min_idx = j
            ai[i], ai[min_idx] = ai[min_idx], ai[i]

    # print(f'#{tc}', *ai[:10])#언패킹 하는 이유?
    print(f'#{tc}', ai[0], ai[1], ai[2], ...,ai[9])  # 언패킹 하는 이유?위와 동일합니다..


