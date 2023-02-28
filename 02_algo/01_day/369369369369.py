N = int(input())


point = ['3','6','9']

for i in range(1,N+1):
    cnt = 0
    for j in str(i):
        if j in point:
            cnt += 1
    if cnt > 0:
        i = '-' * cnt
    print(i, end=' ')

# result = []
# for i in range(1, N + 1):
#     i = str(i)
#     if 3 in i:
#         result.append('-' * (i.count(3)))
#     if 6 in i:
#         result.append('-' * (i.count(6)))
#     if 9 in i:
#         result.append('-' * (i.count(9)))
#     else:
#         print(i)
#오답은 이렇다..