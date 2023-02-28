#테스트 케이스 개수T (1 ≤ T ≤ 50 )
T = int(input())
for tc in range(1,T+1):
# 카드의 장수 N(5 ≤ N ≤ 100 )
    N = int(input())
    arr = list(map(int,input()))
# 0~9 갯수만큼 0이 입력된 리스트 freq
    freq=[0]*10
    for i in arr:
        freq[i] += 1

    cardNo = 0

#
    mostcd = None
    freq = None
    for i in arr:
        for j in arr(i+1,):


# [출력]
  print(f'#{tc} {Mostcd} {freq}')
# 각줄마다"#T"(T는테스트케이스번호)를출력한뒤, 가장많은카드의숫자와장수를차례로출력한다.
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
# 3 T
# 5 N
# 49679 ai
# 5 N
# 08271 ai
# 10 N
# 7797946543 ai
# #1 9 2
# #2 8 1
# #3 7 3
#0~9 10개 리스트 list[0:9]
def frequent(cards):
    N = len(cards)
    frequencypool = []
    for startcard in range(N + 1):
        for nextcard in range(startcard + 1, N + 1):
            if cards[startcard] == cards[nextcard]:
                cards[startcard] += 1  # 빈도수를 arr로 놓고 같은 경우 +=1하면서 출력

    for k in range(N + 1):
        for L in range(k + 1, N + 1):
            if cards[k] < cards[L]:


    return cards[Mostcdn], cdn



T = int(input())
for tc in range(1,T+1):
    Mostcdn = 0 #가장 많이 나온 카드의 종류
    cdn = 0 # 그 카드의 장수
    cards = list(map(int, input().split()))#받은 카드의 리스트화



    cdn, Mostcdn = frequent(cards)

    print(f'#{tc} {Mostcdn} {cdn}')
# 가장 많은 빈도수의 카드{Mostcdn}, 해당 카드의 빈도수{cdn}