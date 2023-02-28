# f(i,k) i = 현재 상태 k = 목표

def f(i, k):
    if i == k:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, k)

A = [10, 20, 30]
B = [0] * 3
f(0, 3)
#B 와 A는 메모리 안의 다른 위치에 저장된 완전히 다른 개체이다

V, E = map(int(input().split()))
arr = list(map(int,input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2 +1]
    adjM[v1][v2] = 1
    adjM[v2][v1] = 1

    adjL[v1].append(v2)
    adjL[v2].append(v1)

print()