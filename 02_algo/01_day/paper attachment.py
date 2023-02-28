#
# def att(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 3
#     return att(n) == att(n-1) + 2*att(n-2)
#
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     pap = att(N)//10
#
#     print(f'{tc} {pap}')


# n = 100
# memo = [0] * (n+1)
# memo[0] = 0
# memo[1] = 1
#
# def fibo1(n):
#     global memo
#     if n<2 or memo[n]:
#         return memo[n]
#     memo[n] = fibo1(n-1) + fibo1(n-2)
#     return memo[n]
#
# T = int(input())
# for tc in range(1,T+1):
#
#
# #memoization
# def att(N):
#
#     n = N//10
#     memoization = [0] * (n+1)
#     memoization[0] = memoization[1] = 1
#     for i in range(2,n+1):
#         memoization[i] = memoization[i-1] + memoization[i-2] *2
#     return memoization[-1]
#
# for t in range(int(input())):
#     print('#{} {}'.format(tc,))
#
# #쓰는 방식에 대한 이해
# #메모이제이션 최적화
# memo = [0]*301#N<= 300이므로
# memo[10] = 1
# memo[20] = 3
#
# def func(n):
#     #기저조건(무한히 반복하는 경우를 막기 위함)
#     if n == 10:
#         return 1
#     elif n == 20:
#         return 3
#     memo[n] = func(n-10) + 2*func(n-20) #재귀호출(점화식 코드)
#     return memo[n]

#3. DP 방식 최적화
#함수 호출을 하여 재귀적으로 푸는 부분을 제거->
memo = [0] * 301
memo[10] = 1
memo[20] = 3
for i in range(30, 301, 10):#기저조건에 10, 20 했고, 10step으로 300까지
    memo[i] = memo[i-10] + 2*memo[i-20]

T = int(input())
for tc in range(1,T+1):

    result = memo[i]
    
print('#{} {}'.format(tc, result))


