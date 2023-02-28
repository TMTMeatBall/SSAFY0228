# def paper_cut(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 3
#     return paper_cut(n-1) + paper_cut(n-2) * 2
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     ans = paper_cut(N//10)
#
#     print("#{} {}".format(tc, ans))
#
# memo = [0]*301
# memo[10] = 1
# memo[20] = 3
# for i in range(30, 301, 10):
#     memo[i] = memo[i-10] + 2*memo[i-20]

def att(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return att(n - 1) + att(n - 2) * 2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = att(N//10)
    print(f'#{tc} {result}')