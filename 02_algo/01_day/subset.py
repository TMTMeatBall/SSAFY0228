T = int(input())

for tc in range (1,T+1):
    N, K = map(int, input().split())
    arr = list(range(1,13))
    result = 0 #받을 결과
    for i in range(1, 1 << len(arr)): #전체 원소 12개의 부분집합 합을 구하고, 거기서 N, K를 만족시킬 때 result에 갯수를 합산하면 된다
        count = 0 #부분집합의 갯수 i 는 ㄴ2^n으로 부분집합의 갯수
        hap = 0 #부분집합의총합
        for j in range(len(arr)): #원소의 수만큼 비트를 비교
            if i & (1 << j): #i의 j번 비트가 1인 경우에, hap와 count에 합산하겠다 j비트 열을 1로 왼쪽으로 이동시킨다에서, i와 2진법 and 비교하고 겹치는 것을 반환

                hap += arr[j]
                count += 1
        if hap == K and count == N:
            result += 1
    print(f'#{tc} {result}')