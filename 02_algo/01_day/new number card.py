#테스트 케이스 개수T (1 ≤ T ≤ 50 )
T = int(input())
for tc in range(1,T+1):
    A=input()
# 카드의 장수 N(5 ≤ N ≤ 100 )
    N = input()
    counts = [0]*10
    list_c=[]
    for i in N:
        list_c.append(int(i))
    for c in list_c:
        counts[c] += 1
    max = 0
    for idx, k in enumerate(counts):
        if max < k:
            max = k
            frequency = idx
            cardname = counts[idx]

        if max != 0 and max == k:
            if frequency < idx:
                frequency = idx

    print(f'#{tc} {frequency} {cardname}')

#반복되는 포인트 파악하고 그만큼 if문을 준다
# 필요한 만큼 인풋 쓰기
#중간중간 print()해서 체크하기
