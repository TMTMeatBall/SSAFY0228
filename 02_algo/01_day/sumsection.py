T = int(input())
for i in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))


    
    maxsum = 0
    minsum = 0
    for l in arr:
        minsum += l
    for j in range(N-M+1): 
        total = 0
        for k in range(j,j+M): #range 는 index주소를 참조해서 움직인다.
            total += arr[k]
        if total > maxsum:
            maxsum = total
        if total < minsum:
            minsum = total



    print(f'#{i} {maxsum - minsum}')