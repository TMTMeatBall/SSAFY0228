# # T = int(input())
# # for tc in range(1, T + 1):
# #     a = list(input())  # 이 값이 초기화 상태랑 얼마나 차이가 있는가
# #     # 최소 수정횟수가 되기 위해서는 왼쪽부터
# #     basezero = [0] * len(a)
# #
# #     cnt = 0
# #     for i in range(len(a)):
# #         if basezero[i] != a[i]:  # 다른 곳이 발견된 때에,
# #             basezero[i:] = a[i]*len(basezero[i:])# 0으로 이뤄진 basezero 를 a[i]로 복제
# #             #i행 이후의 basezero를 전부 다 a[i]값으로 고치기 위해 범위 잡기*중요*
# #             cnt += 1
# #
# #     print(f'#{tc} {cnt}')
# # 질문할 것)
# # 1.처음에 a = list(map(int,input()))으로 받아서 했을 떄에
# # iterable 오류가 나온 이유를 알고 싶습니다.
# ####a=list(input().strip())으로 진행하면 오류가 없어질 것으로 판단됩니다.
# # 2.for 문 만 사용한 case
# T = int(input())
# for tc in range(1, T + 1):
#     a = list(input())  # 이 값이 초기화 상태랑 얼마나 차이가 있는가
#     # 최소 수정횟수가 되기 위해서는 왼쪽부터
#     basezero = [0] * len(a)
#     cnt = 0
#     for i in range(len(a)):
#         if basezero[i] != a[i]:  # 다른 곳이 발견된 때에,
#             for j in range(i, len(a)):
#                 basezero[j] = a[i]
#             cnt += 1
#     print(f'#{tc} {cnt}')
T = int(input())
for tc in range(1, T + 1):
    a = list(input().strip())
    basezero = [0] * len(a)
    cnt = 0
    for i in range(len(a)):
        if basezero[i] != a[i]:
            for j in range(i, len(a)):
                basezero[j] = a[i]
            cnt += 1
    print(f'#{tc} {cnt}')