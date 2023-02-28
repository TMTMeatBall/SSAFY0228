# # #2~n-1나누기를 시도했을 때, 나머지가 0인 경우가 없다면 소수일 것.
# # def is_prime_number(num):
# #     for i in range(2,num):
# #         if num % i == 0:
# #             return False
# #     return True
# # for i in range(2, 100000):
# #     if is_prime_number(i):
# #         print(i)
# #에라스토스테네스의 체를 이용한 소수 판별 알고리즘의 작성
# global prime_numbers
#
# def seive(N):
#     isprime = [True]*(N+1)
#     for i in range(2,N+1):
#         #체크가 안된 값이 있다면 소수
#         if isprime[i] == True:
#
#             for j in range(i*2,N+1,i):
#                 isprime[i] = False #얘네는 배수니까 소수아님
#     return isprime
#
#
#
#
#     print(isprime[21])
#     print(isprime[11])
#     print(isprime[0])
#     print(isprime[1])
#
#     #에라토스테네스의 체
def is_prime_number(n):
    arr = [True]*(n+1)
    arr[0] =False
    arr[1] =False
    for i in range(2,n+1):
        if arr[i] == True :
            j = 2
            while (i*j) <= n:
                arr[i*j] = False
                j += 1
    return arr


arr = is_prime_number(10**6)
for i in range(len(arr)):
    if arr[i] == True:
        print(i, end=' ')
