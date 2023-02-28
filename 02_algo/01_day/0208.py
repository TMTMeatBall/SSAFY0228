# # import sys
# # a=''
# # b='P'
# # c='PY'
# # d='모'
# # print(sys.getsizeof(a))
# #
# # print(sys.getsizeof(b))
# #
# # print(sys.getsizeof(c))
# #
# # print(sys.getsizeof(d))
# #alphabet은 1씩, 한글은 27?
# #1271
# n,m = map(int,input().split())
# print(n//m,n%m,sep='\n')
#2338
# a=int(input())
# b=int(input())
# print(a+b,a-b,a*b,sep='\n')
# #2372
# print('Animal      Count','-'*17,'Chikens       100','Clydesdales     5','Cows           40','Goats          22','Steers          2', sep='\n')
#2420
# N , M = map(int,input().split())
# print(abs(N-M))
#2438
# for i in range(5):
#     print('*'*(i+1))
#2475
# k = list(map(int,input().split()))
# result = (k[0]**2 + k[1]**2+k[2]**2+k[3]**2+k[4]**2)%10
# print(result)
#
# answer = 0
# for i in k
#     answer = i*i
#
# print(answer%10)
# #2753
# A = int(input())
# if not A % 4 and A%100 or A%400 == 0:
#     print(1)
# else:
#     print(0)
#2480
# A, B, C = map(int,input().split())
# if A == B == C :
#     print(10000 + A*1000)
# elif A==B or A ==C :
#     print(1000 + A*100)
# elif B == C:
#     print(1000 + B*100)
# else:
#     print(max(A,B,C)*100)
#2525
# h, m = map(int,input().split())
# t = int(input())
# h += t//60
# m += t%60
# if m >= 60:
#     h += 1
#     m -= 60
# if h >= 24:
#     h -= 24
# print(h,m)
#2884
h,m = map(int,input().split())

print(h,m)
