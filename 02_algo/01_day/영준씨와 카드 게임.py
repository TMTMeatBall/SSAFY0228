T = int(input()) #에러 플래그 설정하기
for tc in range(1, T + 1):
    card = input()
    marks = []
    S = []
    D = []
    H = []
    C = []
    for i in range(0, len(card), 3):  # input된 값들에서 0,3,6의 인덱스값들만 받을 수 있는 range
        marks.append(card[i:i + 3])
    # marks_count = {}
    # for i in marks:
    #     try:
    #         marks_count[i] += 1
    #     except:
    #         marks_count[i] = 1
    # is_error = False  # 에러가 발생한지 유무 파악...
    # for i in marks_count.values():
    #     if i > 1:
    #         print(f'#{tc} error')
    #         is_error = True
    #         break
    # if is_error == False:
    marks.sort()
    is_error = False
    for idx in range(len(marks)-1):
        if marks[idx] == marks[idx + 1]:
            is_error = True
            break

    result = []
    for i in range(len(marks)):
        if marks[i][0] == 'S':
            S.append(marks[i])
        if marks[i][0] == 'D':
            D.append(marks[i])
        if marks[i][0] == 'H':
            H.append(marks[i])
        if marks[i][0] == 'C':
            C.append(marks[i])
    S, D, H, C = 13 - len(S), 13 - len(D), 13 - len(H), 13 - len(C)

    if is_error:
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc}', S, D, H, C)

# 1. 카드의 마크를 보고 구분하여 따로따로 모으기
# 2. 각 구분된 4개 리스트에서 같은 게 있다면 오류 출력하기
# 3. 각 리스트의 갯수만큼 13에서 뺀 것을 출력하기


#     # cntlist = [13, 13, 13, 13]
#     # cards = list(input())
#     # your_deck = []
#     # for i in range(len(cards) - 2):
#     #     if cards[i].isalpha():  # cards[i] 가 알파벳이면..
#     #         your_deck.append(cards[i:i + 3])
#     # for i in range(len(your_deck)):
#     #     your_deck[i][0]
# # S = 0
# # D = 1
# # H = 2
# # C = 3
# # cntlist[i] -= 1 같은 방식으로 빼? 준다?
#     cards = input()
#     S = 13
#     D = 13
#     H = 13
#     C = 13
#     for i in range(len(cards)//3):
#         if cards[i] == 'S':
#
#         if cards[i] == 'D':
#         if cards[i] == 'H':
#         if cards[i] == 'C':
