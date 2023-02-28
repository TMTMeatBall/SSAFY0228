#
# p = 'is' #찾을 패턴
# t = 'this is a book~!'#전체 텍스트
# M = len(p)
# N = len(t)
#
# def BruteForce(p,t):
#     i = 0 #idx t
#     j = 0 #idx p
#     while j<M and i < N:
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#         i = i+1
#         j = j+1
#     if j == M : return i - M #검색 성공
#     else : return -1 #검색 실패

p = 'ab'
t = 'aaaazaaaazaaaab'
M = len(p)
N = len(t)
def bf(p,t, N, M):
    i=0 #t에서 비교위치
    j=0 #p에서  "
    while i < N and j < M:
        if t[i] == p[j]:
            i+=1
            j+=1
        else:
            i = i-j+1
            j = 0
        # if t[i] != p[j]:
        #     i -= j
        #     j -= 1
        # i +=1
        # j +=1
    if j == M:
        return i - M
    else:
        return -1
def bf2(p,t, N, M):
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break

print(bf(p,t,N,M))

def bruteforce(p,t):
    i = 0
    j = 0
    while j < M and i < N:
        for i in range(0,N-M):
            for j in range(0,M-1):
                if t[i+j] != p[j]:
                    break

