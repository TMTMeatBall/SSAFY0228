# # N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
# #
# #
# # [입력]
# #
# # 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
# T = int(input())
# # 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
# N = int(input())
# # 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
# arr = list(map(int, input().split()))
# #로직 처리
# # 3 T
# # 5 N len()
# # 477162 658880 751280 927930 297191 arr
# # 5
# # 565469 851600 460874 148692 111090
# # 10
# # 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
# mxnum = None
# for i in arr:
#     if mxnum is None or mxnum < i:
#         mxnum = i
# print(arr.index(mxnum))

# minnum = None
# for i in arr:
#     if minnum is None or minnum > i:
#         minnum = i 

# answer = print(mxnum-minnum)

# [출력]

#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


T = int(input())
for i in range(1,T+1):

# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
    N = int(input())
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
    arr = list(map(int, input().split()))

    mxnum = None
    for j in arr:
        if mxnum is None or mxnum < j:
            mxnum = j

    minnum = None
    for k in arr:
        if minnum is None or minnum > k:
            minnum = k 
            


    print(f'#{i}',mxnum - minnum)
#문제에서 배운 점
#1.입력값과 출력값이 문제에서 제시한 대로 나오도록 코드를 짤 것
#2. 테스트 케이스란, 해당 문제에서 적용시키는 인풋의 총 갯수를 말할 때 쓰고, 출력에도 for i range 를 통해 인풋 갯수를 돌 변수 i를 통해 아웃풋에 적용 가능하다.
