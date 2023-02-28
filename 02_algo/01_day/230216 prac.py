# # 집합 {1,2,3}의 원소에 대해 각 부분집합에
#
#
# def f(i, k, key):
#     if i == k:
#         s = 0
#         for j in range(k):
#             if bit[j]:
#                 s += A[j]
#         if s == key:
#             for j in range(k):
#                 if bit[j]:
#                     print(A[j], end=' ')
#             if s == key:
#                 return 1
#             return 0
#     else:
#         bit[i] = 1
#         f(i + 1, k, key)
#         bit[i] = 0
#         f(i + 1, k, key)
#
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(A)
# key = 10
# bit = [0] * N
# f(0, N, key)

