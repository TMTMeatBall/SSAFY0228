#10869
#첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B,
#넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
# A,B = list(map(int,input().split()))
# print(A+B, A-B, A*B, A/B, A%B)
#첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B,
#넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
# A,B = list(map(int,input().split()))
# print(A+B, A-B, A*B, A//B, A%B, sep='\n')
#10926
# A = str(input())
# print(A + "??!")
#18108
# A = int(input())
# print(A - int(543))
#3003
# listN = [1,1,2,2,2,8]
# listD = list(map(int,input().split()))
# for i in range(6):
#     print(listN[i] - listD[i],end=' ')
# list_a = list(map(int,input().split()))
#
# def is_zero_subset(list_a):
#     '''
#     부분집합의 합이 0이 되도록 하는 값이 존재하는가 확인하는 함수
#     :param arr: 정수 10개 배열
#     :return: 합이 0이되는 부분집합이 있다
#     '''
#     #부분집합
#     n = len(list_a)
#     #부분집합 만들수 있는 갯수
#     for i in range(1, 1<<n):#부분집합의 시작은 공집합이기때문에, 1부터 시작하게 해서 막아야 한다.
#         for j in range(n):
#             if i & (i <<j):
#                 #이 안에서 합을 진행하고
#                 hap += arr[j]
#         #0이면 True 반환
#         if hap == 0:
#             return True
#     #부분집합의 합으로 0이되는것이 없어서 False 를 반환
#     return False
# print(is_zero_subset())
# #10430
# A,B,C=map(int,input().split())
# print((A+B)%C, ((A%C)+(B%C))%C,(A*B)%C,((A%C)*(B%C))%C, sep='\n')
#2588
# A = int(input())
# B = input()
# print(A*int(B[-1]))
# print(A*(int(B[1])))
# print(A*(int(B[0])))
# print(A*int(B))
#10171
# print('\' ' /\)
# print(" )  ( ')")
# print('(' '/  )')
# print('\(__)|')

# #1330
# A, B = map(int,input().split())
# def differenciate():
#     if A>B:
#         return '>'
#     elif A<B:
#         return '<'
#     else:
#         return '=='
# print(differenciate())