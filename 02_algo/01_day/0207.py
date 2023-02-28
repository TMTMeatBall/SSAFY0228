# #9498
# a = int(input())
# def testgrade(a):
#     if a>=90:
#         return 'A'
#         if a>100:
#             return 'error'
#     elif a>=80:
#         return 'B'
#     elif a>=70:
#         return 'C'
#     elif a>=60:
#         return 'D'
#     else:
#         return 'F'
# print(testgrade(a))
#2753
# arr = list(map(int,input().split()))
# N= int(input())
#
#
#
# for i in range(N-1):
#
#     minidx = i
#
# for j in range (i+1,N):
#
#     if arr[minidx]> arr[j]:
#
#         minidx = i
#
# arr[minidx],arr[i] = arr[i],arr[minidx]
#
# print(arr)

# T=int(input())
# for tc in range(1,T+1):
#     arr = list(map(int,input().split()))
#     for i in range(len(arr)-1):
#         minidx = i
#         for j in range(i+1,len(arr)):
#             if arr[minidx] > arr[j]:
#                 minidx = j
#         arr[i],arr[minidx] = arr[minidx],arr[i]

# print('asdasd','ddwwdd',sep='\n')

T = int(input())
for tc in range(1,T+1):
    #각 테스트 케이스에는 N이 주어진다.
    #각 줄은 '#tc'로 시작, 다음 줄부터 빈칸을 두고 달팽이 숫자를 출력
    N=int(input())
    snail = [[0 for j in range(N)]for i in range(N)]
    def shellline(arr,start,length,num):
        last = start+length-1
        for c in range(start,last+1):
            arr[start][c]
            num +=1
        for r in range(start+1,last+1):

            arr[r][last]=num
            num += 1
        for c in range(last-1,start-1,-1):#역순으로 숫자 들어간다
            arr[last][c] = num
            num += 1
        for r in range(last-1,start,-1):
            arr[r][start] = num
            num += 1
        return num

N=5
print(shellline(snail,0,5,N))

