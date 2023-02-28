import sys
sys.stdin = open('input_01.txt','r')

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n ==1:
                cnt += 1
            else:
                if cnt ==k:
                    ans+= 1
                cnt = 0
    return ans

T = int(input())
for tc in range(1+T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) + [0] ]


    arr_t = list(map(list,zip(*arr)))
    result = count(arr) + count(arr_t)
    print(f'#{tc} {result}')