# n, m = map(int,input().split())
# arr = [0 for _ in range(n)]
# arr = []
# # for i in range(n):
# #     arr.append(list(map(int,input().split())))
#
#
#
# arr2 = [list(map(int,input().split())) for _ in range(n)]
#
# print(arr2)

bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
#부분집합의 반복 loop으로 출력, 0or 1 을 출력하게 하는 것으로
# 부분집합에 들어가거나 들어가지 않는 2가지 경우를 각 자릿수 확정시키고 range2로 넣는다
# def backtrack(a,k,input) :
#     global MAXCANDIDATES
#     c= [0] * MAXCANDIDATES
#
#     if k == input :
#         for i in range(1, k+1):
#             print(a[i], end=' ')
#         print()
#     else:
#         k+=1
#         ncandidates = construct_candidates(a, k, input,c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a,k,input)
for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2 :
                    print(i1,i2,i3)