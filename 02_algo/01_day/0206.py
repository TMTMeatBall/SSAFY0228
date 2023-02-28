#배열 2 
#2차원 배열? - 다차원 list를 말함
#세로(행),가로(열)의 선언을 필요로 함

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
[[1,2,3],[4,5,6],[7,8,9]]
arr = [list(map(int,input())) for _ in range(N)]
[[123],[456],[789]]
#nxm배열의 n*m개의 모든 원소를 빠짐없이 조사하기
for i in range(n): #행을 0으로 고정하고 열 012345---
    for j in range(m):
        Array[i][j]
#열 우선 순회
for j in range(m):
    for i in range(n):
        Array[i][j] #필요연산 수행
#지그재그 순회
for i in range(n):
    for j in range(m):
        Array[i][j + (m-1-2*j)*(i%2)]#열 j의 공식 이해하기
for idx,i in enumerate(range(2,5)):
    idx[0] = idx[i]
#전치 행렬
#i 행 , len(arr)
#j 열 , len(arr[0])
arr = [[1,2,3],[4,5,6][7,8,9]]# 3*3행렬

for i in range(3):
    for j in range(3):
        if i < j :#밖으로 튀어나가지 않게 하는? 계속 지그재그로 돌아오게 하는?
            arr[i][j], arr[j][i] = arr[j][i],arr[i][j]
#부분집합에 관해서
bit = [0, 0, 0, 0] #이진수로 표현 이 경우 2^3,2^2,2^1,2^0으로
for i in range(2):
    bit[0] = i 
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2]=k
            for l in range(2):
                bit[3] = l
                print_subset(bit)

arr = [3,6,7,1,5,4]
n = len(arr)
# for i in range(1<<n) : #?가 1인지 0인지?
#     for j in range(n):
#         if i and (1<<j):
#             print(arr[j],end=', ')
#     print()
# print()
#10개의 정수를 입력받아 부분집합의 합이 0이 되는 
# 것이 존재하는지를 계산하는 함수를 작성하기
list_a = list(map(int,input().split()))

def is_zero_subset(list_a):
    '''
    부분집합의 합이 0이 되도록 하는 값이 존재하는가 확인하는 함수
    :param arr: 정수 10개 배열
    :return: 합이 0이되는 부분집합이 있다
    '''
    #부분집합
    n = len(list_a)
    #부분집합 만들수 있는 갯수
    for i in range(1, 1<<n):#부분집합의 시작은 공집합이기때문에, 1부터 시작하게 해서 막아야 한다.
        for j in range(n):
            if i & (1 <<j):
                #이 안에서 합을 진행하고
                hap += arr[j]
        #0이면 True 반환
        if hap == 0:
            return True
    #부분집합의 합으로 0이되는것이 없어서 False 를 반환
    return False
        

#델타를 이용한 2차 배열 탐색(이미지 처리 알고리즘을 짤 때 이런 순회 배열을 사용한다.)
#어떤 i,j에서
di = [0,1,0,-1]
dj = [1, 0, -1, 0]
N=3
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni, nj = i+di[k],j+dj[k]
            if 0<= ni<N and 0<=nj<N:
                print(i, j, ni, nj)

N=3
for i in range(N):
    for j in range(N):
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di , j+dj
            if 0<=ni<N and 0<=nj<N:
                print(i,j,ni,nj)

arr[0...N-1][0...N-1]

A=[1,2,3,4]#부분집합
bit = [0]*4#각 원소의 배열을 말하는 집합
for i in range(i):
    bit[0]=i
    for j in range(2):
        bit[1]=j
        for k in range(2):
            bit[3] = k
            for l in range(2):
                bit[3]=l
                print(bit, end=' ')
                s=0
                for p in range(4):
                    if bit[p]:
                        print(A[p], end=' ')
                        s += A[p]
                print(s)

arr = [3,6,7,1,5,4]

n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i and (1 <<j):
            print(arr[j], end=', ')
    print()
print()
#델타, 이차원배열 안에서 배열, 원소를 어떻게 할 것인가
