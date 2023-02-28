#대표적 그리디 알고리즘 문제
#매순간에 선택/방법이 최적인 답을 출력
#베이비진 문제 : 탐욕x 순열로 카드뽑기 trippet
T = int(float(input())) #테스트케이스
for tc in range(1,T+1):
    # 두 플레이어가 갖는 카드 리스트 (0~9:길이가 10임)
    p1_count = [0]*10
    p2_count = [0]*10
    
    #숫자 리스트를 저장할 리스트
    cards = list(map(int,input().split()))
    #베이비진인지 확인해서 True, False를 함수
    #run trippet 이라면 True, (아니라면 False 반환)
    #greedy 알고리즘 처럼 작성하기 ->매순간 최선의 선택을 -> '체크 하는 순간' 입력이 들어온 카드를 기준으로
    def isBabygin(counts,current):
        '''
        :param counts : 플레이어의 카드 카운트 리스트
        :param current : 방금 입력받은 카드 번호
        :return : 베이비진이면 T 아니면 F를 반환
        '''
        #run 판별로직
        if counts[current]>= 3:
            return True
        #trippet 판별
        #c, c+1, c+2 카드존재 확익
        if (current < 8) and counts[current] and counts[current+1] and counts[current+2]:
            return True
        #c-1 c c+1
        if (1< current <9) and counts[current-1] and counts[current] and counts[current+1]:
            return True
        #c-2 c-1 c
        if (2 < current) and counts[current-2] and counts[current-1] and counts[current]:
            return True
        else:
            return False
    #숫자 리스트를 순회하면 p1,p2순서대로 카드를 나눠준다
    # for idx in range(len(cards)):
    #     if idx % 2 == 0 :
    #         p1_counts[cards[idx]] +=1
    result = 0
    for idx, card in enumerate(cards):
        if idx % 2 == 0:
            p1_count[card] +=1
            #베이비진인지 판별하는 로직 (run, trippet ... 판단 로직 ... )
            if isBabygin(p1_count,card):
                # True -> 해당 플레이어가 승리했다고 결과를 반환하고,
                result = 1
                break
        else:
            p2_count[card] +=1
            if isBabygin(p2_count,card):
                result = 2
                break

    print(f'#{tc} {result}')